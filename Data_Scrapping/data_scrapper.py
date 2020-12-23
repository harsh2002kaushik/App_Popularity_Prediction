import numpy
import pandas as pd
import selenium
from selenium import webdriver
import time 

top_grossing_games = 'https://play.google.com/store/apps/collection/cluster?clp=0g4YChYKEHRvcGdyb3NzaW5nX0dBTUUQBxgD:S:ANO1ljLhYwQ&gsr=ChvSDhgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljIKta8&hl=en_IN'
top_free_games = 'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c&hl=en_IN'
top_paid_games = 'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfcGFpZF9HQU1FEAcYAw%3D%3D:S:ANO1ljLtt38&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljJCqyI&hl=en_IN'
all_games = [top_paid_games,top_free_games,top_grossing_games]
driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
#driver.maximize_window()
games = []

for a in all_games:
    driver.get(a)
    for c in range(4):
        driver.execute_script("window.scrollTo(0,10000)")
        time.sleep(3)
    
    game_list = driver.find_elements_by_xpath('//div[@class="WsMG1c nnK0zc"]')
    game_names = []
    
    for i in game_list:
        game_names.append(i.text)  
   
    for b in range(len(game_names)):
         try:
            game_link=driver.find_element_by_link_text(game_names[b])
            driver.execute_script("arguments[0].click();",game_link) 
            
        except:
            driver.refresh()
            time.sleep(1)
            driver.refresh()
            
            for c in range(5):
                driver.execute_script("window.scrollTo(0,10000)")
                time.sleep(3)
                
            game_link=driver.find_element_by_link_text(game_names[b])
            driver.execute_script("arguments[0].click();",game_link)
            
        time.sleep(3)
        
        try:
            editor_choice = driver.find_element_by_xpath('.//span[@class="dMMEE"]').text
        
        except:
            editor_choice = '0'
        
        time.sleep(3)
        
        game_type = driver.find_elements_by_xpath('.//a[@class="hrTbp R8zArc"]')
        
        try:
            for d in range(len(game_type)):
                game_type[d] = game_type[d].text
        except:
            time.sleep(3)
            for d in range(len(game_type)):
                game_type[d] = game_type[d].text
        
        try:
            time.sleep(2)
            comment = driver.find_element_by_xpath('.//span[@class="EymY4b"]').text
        except:
            comment = 'not given'

        try:
            prices = driver.find_element_by_xpath('.//button[@class="LkLjZd ScJHi HPiPcc IfEcue  "]').text 
        except:
            prices= 0

        gen_info = driver.find_elements_by_class_name('BgcNfc')
        gen_info_values = driver.find_elements_by_class_name('htlgb')
        games_info = {}
        
        for e in range(len(gen_info)):
            games_info[gen_info[e].text] = gen_info_values[2*e].text
        
        try:
            Updated = games_info['Updated']
        except: 
            Updated = 'not updated'
        
        try:
            Size = games_info['Size']
        except:
            Size = 'Varies with device'
        
        try:
            Installs = games_info['Installs']
        except:
            Installs = -1
        
        try:
            Version = games_info['Current Version']
        except:
            Version = 'unavailable'
        
        try:
            Android = games_info['Requires Android']
        except:
            Android = '0'
        
        try:
            Rating = games_info['Content rating']
        except:
            Rating = 'unavailable'
        
        try:
            Elements = games_info['Interactive Elements']
        except:
            Elements = 'none'
        
        try:
            Purchases = games_info['In-app Products']
        except:
            Purchases = 'none'
        
        try:
            Offered_by = games_info['Offered By']
        except:
            Offered_by = 'not given'
        
        try:
            Developer = games_info['Developer']
        except:
            Developer = 'none'
        
        games.append({
                 '_editors_choice':editor_choice,
                 '_game_types':game_type,
                 '_comments':comment,
                 '_price':prices,
                 '_updated':Updated,
                 '_size':Size,
                 '_installs':Installs,
                 '_version':Version,
                 '_required_android':Android,
                 '_content_rating':Rating,
                 '_interactive_elements':Elements,
                 '_in_app_products':Purchases,
                 '_offered_by':Offered_by,
                 '_developer':Developer})      

        driver.back()
        
df = pd.DataFrame(games)

df.to_csv(r'C:\Users\harsh\Desktop\Extracted_Games.csv',index = False)
