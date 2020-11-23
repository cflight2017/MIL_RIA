#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:39:20 2020

@author: christienwright
"""

#%%
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
import numpy as np

#Functions for NBA API Pull

class NBA_API:
    #Team Schedule
    def get_team_schedule(season : int, team : str):
        global schedule, data
        
        df_sched = pd.DataFrame()
    
        link = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/' + str(season) + '/teams/' + team + '_schedule.json'
        
        r = requests.get(link)
        
        data = r.json()
        
        df = pd.DataFrame(data['gscd']['g'])
        
        for i in range(len(df)):
        
            v = data['gscd']['g'][i]['v']
            
            h = data['gscd']['g'][i]['h']
            
            df_ =  pd.DataFrame(dict(df.iloc[i]), index = [i])
           
            df_['tmp'] = 1
            
            h = pd.DataFrame(h,index = [i])
            
            h['tmp'] = 1
            
            h = h.rename(columns = {"tid":"tid_home", "re":"re_home", "ta":"ta_home", "tn":"tn_home", "tc":"tc_home",
                                "s":"s_home"})
            
            v = pd.DataFrame(v,index = [i])
            
            v['tmp'] = 1
            
            v = v.rename(columns = {"tid":"tid_vis", "re":"re_vis", "ta":"ta_vis", "tn":"tn_vis", "tc":"tc_vis",
                                "s":"s_vis"})
            
            df1 = df_.merge(h)
            
            df_schedule = df1.merge(v)
            
            df_sched = df_sched.append(df_schedule)
            
        
        schedule = df_sched.drop(columns = ['bd', 'v', 'h'])
        return schedule
        
    
    
    def get_roster(season : int, team : str):
        global roster, data
        
        link = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/'+ str(season) + '/teams/' + team + '_roster.json'
        
        r = requests.get(link)
        
        data = r.json()
        
        print(data)
        
        team_info = pd.DataFrame([[data['t']['ta'], data['t']['tc'], data['t']['tid'], data['t']['tn']]], columns = ['ta', 'tc', 'tid', 'tn'])
        
        players = pd.DataFrame(data['t']['pl'])
        
        team_info['key'] = 0
        
        players['key'] = 0
        
        df = pd.merge(team_info, players, how ='inner', on = 'key')
        
        roster = df.drop(columns = ['key'])
        
        return roster
    
    
    
#Player Averages Data NBA   

    def get_player_stats(season : int, team : str):
        global player_stats, data
        
        link = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/' + str(season) + '/teams/' + team + '/player_averages_01.json'
        
        r = requests.get(link)
        
        data = r.json()
        
        player_stats = pd.DataFrame()
        
        for i in range(len(data['tpsts']['pl'])):
            player = pd.DataFrame([[data['tpsts']['pl'][i]['fn'],data['tpsts']['pl'][i]['ln'],data['tpsts']['pl'][i]['pid'],data['tpsts']['pl'][i]['pos'], 0]] , columns = ['fn', 'ln', 'pid', 'pos', 'key'])
            
            avg = pd.DataFrame([data['tpsts']['pl'][i]['avg']])
            
            avg['key'] = 0
            
            totals = pd.DataFrame([data['tpsts']['pl'][i]['tot']])
            
            totals['key'] = 0
            
            ps = pd.merge(player, avg, on = 'key')
            
            stats = pd.merge(ps, totals, on = 'key')
            
            player_stats = player_stats.append(stats)
        
        player_stats = player_stats.drop(columns = ['key'])
        
        return player_stats
            
#Play by Play

    def get_pbp(season : int, game_id : int):
        global pbp_clean, pbp_data
        link = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/' + str(season) + '/scores/pbp/' + str(game_id) + '_full_pbp.json'
        
        r = requests.get(link)
        
        pbp_data = r.json()

        pbp_clean = pd.DataFrame()
        for i in range(len(pbp_data['g']['pd'])):
            gcode = pbp_data['g']['gcode'] #get game code for link for box score
            gid = pbp_data['g']['gid'] #Game id for id
            mid = pbp_data['g']['mid'] #media id ?
            period = pbp_data['g']['pd'][i]['p']  #Loop through each period
            game_info = pd.DataFrame(np.array([[gcode, gid, mid, period]]), columns = ['gcode', 'gid', 'mid', 'period']) #form a dataframe
            game_info['temp'] = 0 #temp key for merge
            plays = pd.DataFrame(pbp_data['g']['pd'][i]['pla'])  #Get pbp period info
            plays['temp'] = 0  #merge on plays for that particular period
            
            pbp = pd.merge(game_info, plays, on = 'temp')
            
            
            game_event_details = pd.read_excel('~/WNBA Shot Chart App /WNBA_Shot_Chart_App/game_event_details.xlsx', sheet_name = 'Action Types')
            
            pbp_update = pd.merge(pbp, game_event_details, on = ['etype', 'mtype'], how = 'left')
            
            pbp_sort = pbp_update.sort_values(by = ['evt']) 
            
            pbp_clean = pbp_clean.append(pbp_sort)
                
        pbp_clean = pbp_clean.drop(columns = ['temp'])
        
        return pbp_clean
    

    
    

    
                           