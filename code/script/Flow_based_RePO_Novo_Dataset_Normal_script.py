import tensorflow as tf
import numpy as np
import os
import sys
import time
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras import Model
import pandas as pd

#label_names=['LDAP','NetBIOS','MSSQL','Portmap','Syn','UDP','UDPLag']

def get_test_set():
    test_files = ['../../data/novoDataset/LDAP.csv',
                '../../data/novoDataset/MSSQL.csv',
                '../../data/novoDataset/NetBIOS.csv',
                '../../data/novoDataset/Portmap.csv',
                '../../data/novoDataset/Syn.csv',
                '../../data/novoDataset/UDP.csv',
                '../../data/novoDataset/UDPLag.csv']

    ## será o mesmo train min e max, pois são dados normais!
    train_min = np.load('../../data/flow_based/x_train_meta/train_min.npy')
    train_max = np.load('../../data/flow_based/x_train_meta/train_max.npy')
    

    print(f'Valor minimo treino:{train_min}\nValor maximo treino{train_max}')
    print(f'Tamanho minimo treino:{len(train_min)}\nTamanho maximo treino{len(train_max)}')
    x_test_all = []
    y_test_all = []
    all_label_set = []
    for i in range(len(test_files)):
        print (i,test_files[i])
        url_data = test_files[i]
        df = pd.read_csv(url_data)

        feats = df.iloc[:,8:]
        ds_port = df.iloc[:,5]
        df = pd.concat([ds_port,feats],axis=1)

        labels = df.iloc[:,-1].values
        label_set = set(labels)
        all_label_set.append(label_set)

        all_feats = df.iloc[:,:-1].astype(np.float64).values
        known_data_IDs =(np.any(np.isinf(all_feats),axis=1) + np.any(np.isnan(all_feats),axis=1))==False
        x_test = all_feats[known_data_IDs]
        y_test = df.iloc[:,-1].values
        y_test = y_test[known_data_IDs]
        x_test = (x_test - train_min)/(train_max - train_min+1e-6)
        x_test_all.append(x_test)
        y_test_all.append(y_test)
    x_test = np.concatenate(x_test_all,axis=0).astype(np.float32)
    y_test = np.concatenate(y_test_all,axis=0)
    
    return x_test, y_test

def get_scores(x_test):
    plus_batch_size = 100
    score_np = np.zeros(len(x_test)+plus_batch_size)
    begin_time = time.time()
    flag=False
    for i in range(0,len(x_test),plus_batch_size):
        if i%100000==0:
            print (i,time.time() - begin_time)
        sample = x_test[i:i+plus_batch_size]
        if len(sample)<plus_batch_size:
            temp = np.zeros((plus_batch_size-len(sample),num_input),np.float32)
            sample = np.concatenate((sample,temp))
        sample = sample.reshape(-1,1,num_input) +  np.zeros((100,num_input),np.float32)
        sample = sample.reshape(-1,num_input)
        rec_error = test_step(sample)
        rec_error_np = rec_error.numpy().reshape(-1,5,20)
        best_rec_err_val =  np.min(rec_error_np,axis=-1)
        score_np[i:i+plus_batch_size] = np.sum(best_rec_err_val,axis=1)
    score_np = score_np[:len(x_test)]
    print (i,time.time() - begin_time)
    return score_np

@tf.function
def test_step(x):
    mask = tf.random.uniform(shape=[100*100,num_input])
    mask = tf.cast((mask>0.75),tf.float32)
    partial_x = mask*x
    rec_x = model(partial_x, training=False)
    score = tf.reduce_mean(tf.square(rec_x - x),axis=1)
    return score


if __name__ == "__main__":
    tempoInicial=time.time()
    print(f"INICIO TESTE RePO FLOW BASED NORMAL NovoDataset\n{time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())}\n")
    model = tf.keras.models.load_model('../../models/flow_based_model/')

    x_test, y_test = get_test_set()
    num_input = x_test.shape[1]
    print(f'x_test:{x_test.shape}\ny_test:{y_test.shape}\n')
    label_names = ['BENIGN','LDAP','NetBIOS','MSSQL','Portmap','Syn','UDP','UDPLag'] #ataques do novo dataset
    all_scores = get_scores(x_test)
    print(f'scores independente do fpr\n{all_scores}')
    fpr = 0.01
    benign_scores = all_scores[y_test=='BENIGN']
    print(f'scores com fpr==0.01\n{benign_scores}')
    benign_scores_sorted = np.sort(benign_scores)
    thr_ind = int(np.ceil(len(benign_scores_sorted)*0.01))
    thr = benign_scores_sorted[-thr_ind]
    print (f'threshold atual->{thr}\n')

    for i in range(len(label_names)):
    #### Exclude web attacks from results
        if label_names[i].find('Web')>=0:
            continue
        scores = all_scores[y_test==label_names[i]]
        if i==0:
            fpr = "{0:0.4f}".format(np.sum(scores>=thr)/(0. + len(scores)))
            print('FPR:',fpr)
        else:
            tpr = "{0:0.4f}".format(np.sum(scores>=thr)/(0. + len(scores)))
            print(label_names[i]+':',tpr)
    print(f"FIM TESTE RePO FLOW BASED NORMAL NovoDataset \nTempo decorrido:{(time.time()-tempoInicial)}seg\n{time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())}")

