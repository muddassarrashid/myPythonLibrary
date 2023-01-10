#!/usr/bin/env python

# Importing Libraries
import pandas as pd
import numpy as np

# Defining Functions

def Read_CSV(filepath):
    '''Reads the csv table that that the generic tracking algorithm saves. Function uses predefined '''
    # Defining the headers for the EVK CSV files
    csv_headers = ['x_floor', 'y_floor', 't_stamp', 'x', 'y', 'bb_height', 'bb_width', 'id_particle', 'event_number']

    #loading csv file as panda dataframe
    return pd.read_csv(filepath, delimiter=',', names=csv_headers)

def get_UniqueIDs(DataTable):
    '''
    Determines all the different ID of particles being tracked
    '''
    IDs, counts = np.unique(DataTable['id_particle'], return_counts=True)
    return IDs, counts

def get_modeID(DataTable):
    '''Determines the mode of the id_particles
    '''
    return DataTable['id_particle'].mode()

def filter_DataTable_By_ID(DataTable, ID):
    ''' With designated id the datatable is filter'''
    return DataTable.loc[(DataTable['id_particle'].values == ID).T]


def getXYtime(DataTable):
    ''' This extracts X position, Y position and time axis from datatable'''
    X = DataTable.x;
    Y = DataTable.y
    time = DataTable.t_stamp*1e-6

    return X,Y,time
