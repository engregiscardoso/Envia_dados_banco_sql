# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:04:14 2023

@author: REGIS CARDOSO
"""


import pandas as pd
import numpy as np
import statistics
import math
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from datetime import timedelta, datetime
from scipy.fftpack import fft, fftfreq
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
import sqlalchemy as sqldb
from datetime import timedelta, datetime
import struct



# Função de conexão
def conexao():
    
    #### Parâmetros de CONEXÃO #####
    server = '10.61.xxx.xx'
    database = 'data_base_nome'
    username = 'username'
    password = 'password'
    engineString = 'mssql+pyodbc://'+username+':'+password+'@'+server+':1433/'+database+'?driver=ODBC Driver 17 for SQL Server'

    engine = sqldb.create_engine(engineString)
    conectado = engine.connect()
    return conectado



# Função envio de dados
def envia_dados(parametros_tabela):
       
    string_envio = "INSERT INTO colocar aqui a tabela que os valores serão inseridos (colocar aqui os parametros da taleba) VALUES ('" + parametros_tabela + ")"

    envia = conectado.execute(string_envio)
    
    envia.close





df= pd.read_csv('seleciona arquivo de dados.csv', sep=',')



#### Parametros para ENVIO DE DADOS #####
parametros_tabela = 'parametros_tabela'




connection = conexao()  

envia_dados(parametros_tabela)
