# List of packages to import for this module
from pathlib import Path
import pandas as pd
import numpy as np

##############################################################################################################################

def get_csv(string,na_values = None):

    path = str(Path(__file__).parent)+'/data/'+string+'.csv'
    df = pd.read_csv(path,header=0,na_values = na_values)
    return df

##############################################################################################################################
def circuit_csv():
    return get_csv('circuits')
##############################################################################################################################
def constructor_results_csv():
    return get_csv('constructor_results',na_values = r"\N")
##############################################################################################################################
def constructor_standings_csv():
    return get_csv('constructor_standings')
##############################################################################################################################
def constructors_csv():
    return get_csv('constructors')
##############################################################################################################################
def driver_standings_csv():
    return get_csv('driver_standings')
##############################################################################################################################
def drivers_csv():
    # dob as date
    drivers = get_csv('drivers',na_values = r"\N")
    drivers['dob'] = pd.to_datetime(drivers['dob'])
    return drivers
##############################################################################################################################
def lap_times_csv():
    lap_times =  get_csv('lap_times')
    lap_times['time_seconds'] = lap_times['milliseconds']/1000
    return lap_times
##############################################################################################################################
def pit_stops_csv():
    return get_csv('pit_stops')
##############################################################################################################################
def qualifying_csv():
    qualifying =  get_csv('qualifying',na_values = r"\N")
    for i in ['q1','q2','q3']:
        qualifying[i+'_seconds'] = qualifying[i].str.split('[:|.]').apply(lambda x: float(str(60*int(x[0])+int(x[1]))+'.'+x[2]) if isinstance(x, list) else np.nan)
    return qualifying
##############################################################################################################################
def races_csv():
    races = get_csv('races')
    races['date'] = pd.to_datetime(races['date'])
    # time to time
    return races
##############################################################################################################################       
def results_csv():
    results = get_csv('results',na_values = r"\N")
    mask = (results['driverId'] == 830) & (results['raceId'] == 1062)
    results.loc[mask,'fastestLapTime'] = '1:20.945'
    results['seconds'] = results['milliseconds']/100
    results['fastestLapTime'] = results['fastestLapTime'].str.split('[:|.]').apply(lambda x: float(str(60*int(x[0])+int(x[1]))+'.'+x[2]) if isinstance(x, list) else np.nan)
    return results
##############################################################################################################################
def seasons_csv():
    return get_csv('seasons')
############################################################################################################################## 
def status_csv():
    return get_csv('status')
##############################################################################################################################