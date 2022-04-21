import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nsepy import get_history
from nsepy.history import get_price_list
from datetime import date, timedelta
import time
import talib as ta
from pynse import *
nse = Nse()

def sec(sect=None):
    for j in sect:
        try:
            j = get_history(symbol=j,start=init_date,end=today_date)
            init_chng_stock = j.head(1)['Close'][0]
            final_chng_stock = j.tail(1)['Close'][0]
            per_chng_stock = np.round(((final_chng_stock - init_chng_stock)/init_chng_stock)*100,2)
            op_sector_stock.append(per_chng_stock)
        except:
            continue
        finally:
            continue
    op_stock_df = pd.DataFrame({'Symbol': sect, '%Chng': op_sector_stock})
    st.write('Stock list of given index')
    st.table(op_stock_df)
    max_chng_stk = np.array(op_sector_stock[:]).max()
    st.write('Outperforming stock of index')
    op_stock = op_stock_df.loc[op_stock_df['%Chng']==max_chng_stk]
    st.table(op_stock) 
    op_stock_index = op_stock.index[0]
    op_stock.loc[op_stock_index,'Symbol']
    op_stock_df = get_history(symbol=op_stock.loc[op_stock_index,'Symbol'],start=init_date,end=today_date)
    op_stock_df['Index'] = op_stock_df.index
    op_stock_drop_col_df = op_stock_df.drop(['Turnover','Deliverable Volume','%Deliverble',
                                'VWAP','Trades','Index','Series','Prev Close','Last'],axis=1)
    op_stock_drop_col_res_ind_df = op_stock_drop_col_df.reset_index()
    st.table(op_stock_drop_col_res_ind_df)
    op_stock_drop_col_df['Date'] = op_stock_drop_col_df.index
    chart_ = op_stock_drop_col_df.loc[:,['Date','Close']]
    # fig = plt.figure(figsize=(12,6))
    # plt.xlabel('Day')
    # plt.ylabel('Close')
    # plt.plot(chart_['Close'])
    # plt.scatter(chart_['Close'])
    # st.pyplot(fig)
    st.line_chart(chart_.Close)


def sec_2(sect=None):
    for j in sect:
        try:
            j = get_history(symbol=j,start=init_date,end=today_date)
            init_chng_stock = j.head(1)['Close'][0]
            final_chng_stock = j.tail(1)['Close'][0]
            per_chng_stock = np.round(((final_chng_stock - init_chng_stock)/init_chng_stock)*100,2)
            op_sector_stock.append(per_chng_stock)
        except:
            continue
        finally:
            continue
    op_stock_df = pd.DataFrame({'Symbol': sect, '%Chng': op_sector_stock})
    st.write('Stock list of given index')
    st.table(op_stock_df)
    min_chng_stk = np.array(op_sector_stock[:]).min()
    st.write('Underperforming stock of index')
    op_stock = op_stock_df.loc[op_stock_df['%Chng']==min_chng_stk]
    st.table(op_stock) 
    op_stock_index = op_stock.index[0]
    op_stock.loc[op_stock_index,'Symbol']
    op_stock_df = get_history(symbol=op_stock.loc[op_stock_index,'Symbol'],start=init_date,end=today_date)
    op_stock_df['Index'] = op_stock_df.index
    op_stock_drop_col_df = op_stock_df.drop(['Turnover','Deliverable Volume','%Deliverble',
                                'VWAP','Trades','Index','Series','Prev Close','Last'],axis=1)
    op_stock_drop_col_res_ind_df = op_stock_drop_col_df.reset_index()
    st.table(op_stock_drop_col_res_ind_df)
    op_stock_drop_col_df['Date'] = op_stock_drop_col_df.index
    chart_ = op_stock_drop_col_df.loc[:,['Date','Close']]
    # fig = plt.figure(figsize=(12,6))
    # plt.xlabel('Day')
    # plt.ylabel('Close')
    # plt.plot(history,chart_['Close'])
    # plt.scatter(history,chart_['Close'])
    # st.pyplot(fig)
    st.line_chart(chart_.Close)

def vol(sect=None,lst=None,sec=None):
    for k in sect: 
        try:
            k = get_history(symbol=k,start=init_date,end=today_date)
            lst.append(np.round((np.sum(k['Volume'].values)/k.shape[0]),2))
        except:
            continue
        finally:
            continue
    df = pd.DataFrame({'Stock':sect,'Avg. Volume':lst,'Sector':sector[sec]})
    arr = np.array(lst[:]).max()
    f_df = df.loc[df['Avg. Volume'] == arr]
    f_df_in = f_df.reset_index()
    stock_.append(f_df_in.loc[0,'Stock'])
    avg_vol.append(f_df_in.loc[0,'Avg. Volume'])
    sector_.append(f_df_in.loc[0,'Sector'])

def file_read():
    global sector
    sector = ['NIFTY', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG',
        'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 'NIFTY REALTY', 'NIFTY PVT BANK']
    global auto
    auto = pd.read_csv('ind_niftyautolist.csv')
    global bank
    bank = pd.read_csv('ind_niftybanklist.csv')
    global energy
    energy = pd.read_csv('ind_niftyoilgaslist.csv')
    global fin_serv
    fin_serv = pd.read_csv('ind_niftyfinancelist.csv')
    global fmcg
    fmcg = pd.read_csv('ind_niftyfmcglist.csv')
    global it
    it = pd.read_csv('ind_niftyitlist.csv')
    global media
    media = pd.read_csv('ind_niftymedialist.csv')
    global metal
    metal = pd.read_csv('ind_niftymetallist.csv')
    global pharma
    pharma = pd.read_csv('ind_niftypharmalist.csv')
    global psu_bank
    psu_bank = pd.read_csv('ind_niftypsubanklist.csv')
    global pvt_bank
    pvt_bank = pd.read_csv('ind_nifty_privatebanklist.csv')
    global realty
    realty = pd.read_csv('ind_niftyrealtylist.csv')

def progress_bar():
    st.write('Gathering information...')
    progress = st.progress(0)
    for pro in range(100):
        time.sleep(0.01)
        progress.progress(pro+1)

def dict_read():
    global sector_adv_dec
    sector_adv_dec = st.sidebar.selectbox('select sector',['NIFTY', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG','NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 
    'NIFTY REALTY', 'NIFTY PVT BANK'])
    
    global sec_dic
    sec_dic = {'NIFTY':IndexSymbol.Nifty50, 'NIFTY AUTO':IndexSymbol.NiftyAuto, 
    'NIFTY BANK':IndexSymbol.NiftyBank, 'NIFTY ENERGY':IndexSymbol.NiftyEnergy, 
    'NIFTY FIN SERVICE':IndexSymbol.NiftyFinService, 'NIFTY FMCG':IndexSymbol.NiftyFmcg,
    'NIFTY IT':IndexSymbol.NiftyIt, 'NIFTY MEDIA':IndexSymbol.NiftyMedia, 'NIFTY METAL':IndexSymbol.NiftyMetal, 'NIFTY PHARMA':IndexSymbol.NiftyPharma, 'NIFTY PSU BANK':IndexSymbol.NiftyPsuBank,
    'NIFTY PVT BANK':IndexSymbol.NiftyPvtBank,'NIFTY REALTY':IndexSymbol.NiftyRealty}


if __name__ == '__main__': 

    market = nse.market_status()
    market_time = market['marketState'][0]['marketStatus']

    date_stamp = time.strftime('%a , %d  %b %Y , %I:%M %p',time.localtime())
    time_stamp = ('%H:%M',time.localtime())
    # d = st.columns(3)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write('Market Status: ',market_time)
    with col3 :
        st.write(date_stamp)

    c1,c2,c3,c4,c5,c6,c7,c8 = st.columns(8)
    # c9,c10,c11,c12,c13 = st.columns(5)
    
    with c1:
        nifty =  nse.get_indices(IndexSymbol.Nifty50)
        st.write('NIFTY50')
        st.write(nifty['last'][0])
        st.write(nifty['percentChange'][0],'%')
        st.write(nifty['variation'][0])

    with c2:
        niftybank =  nse.get_indices(IndexSymbol.NiftyBank)
        st.write('NIFTYBANK')
        st.write(niftybank['last'][0])
        st.write(niftybank['percentChange'][0],'%')
        st.write(niftybank['variation'][0])
    # with c3:
    #     niftyauto =  nse.get_indices(IndexSymbol.NiftyAuto)
    #     st.write('NIFTYAUTO')
    #     st.write(niftyauto['last'][0])
    #     st.write(niftyauto['percentChange'][0],'%')
    #     st.write(niftyauto['variation'][0])
    # with c4:
    #     niftyenergy =  nse.get_indices(IndexSymbol.NiftyEnergy)
    #     st.write('NIFTYENERGY')
    #     st.write(niftyenergy['last'][0])
    #     st.write(niftyenergy['percentChange'][0],'%')
    #     st.write(niftyenergy['variation'][0])
    # with c5:
    #     niftyfinserv =  nse.get_indices(IndexSymbol.NiftyFinService)
    #     st.write('NIFTYFINSERV')
    #     st.write(niftyfinserv['last'][0])
    #     st.write(niftyfinserv['percentChange'][0],'%')
    #     st.write(niftyfinserv['variation'][0])
    # with c6:
    #     niftyfmcg =  nse.get_indices(IndexSymbol.NiftyFmcg)
    #     st.write('NIFTYFMCG')
    #     st.write(niftyfmcg['last'][0])
    #     st.write(niftyfmcg['percentChange'][0],'%')
    #     st.write(niftyfmcg['variation'][0])
    # with c7:
    #     niftyit =  nse.get_indices(IndexSymbol.NiftyIt)
    #     st.write('NIFTYIT')
    #     st.write(niftyit['last'][0])
    #     st.write(niftyit['variation'][0])
    #     st.write(niftyit['percentChange'][0],'%')    
    # with c8:
    #     niftymedia =  nse.get_indices(IndexSymbol.NiftyMedia)
    #     st.write('NIFTYMEDIA')
    #     st.write(niftymedia['last'][0])
    #     st.write(niftymedia['variation'][0])
    #     st.write(niftymedia['percentChange'][0],'%')
    # with c9:
    #     niftymetal =  nse.get_indices(IndexSymbol.NiftyMetal)
    #     st.write('NIFTYMETAL')
    #     st.write(niftymetal['last'][0])
    #     st.write(niftymetal['variation'][0])
    #     st.write(niftymetal['percentChange'][0],'%')
    # with c10:
    #     niftypharma =  nse.get_indices(IndexSymbol.NiftyPharma)
    #     st.write('NIFTYPHARMA')
    #     st.write(niftypharma['last'][0])
    #     st.write(niftypharma['variation'][0])
    #     st.write(niftypharma['percentChange'][0],'%')
    # with c11:
    #     niftypsubank =  nse.get_indices(IndexSymbol.NiftyPsuBank)
    #     st.write('NIFTYPSUBANK')
    #     st.write(niftypsubank['last'][0])
    #     st.write(niftypsubank['variation'][0])
    #     st.write(niftypsubank['percentChange'][0],'%')
    # with c12:
    #     niftypvtbank =  nse.get_indices(IndexSymbol.NiftyPvtBank)
    #     st.write('NIFTYPVTBANK')
    #     st.write(niftypvtbank['last'][0])
    #     st.write(niftypvtbank['variation'][0])
    #     st.write(niftypvtbank['percentChange'][0],'%')
    # with c13:
    #     niftyrealty =  nse.get_indices(IndexSymbol.NiftyRealty)
    #     st.write('NIFTYREALTY')
    #     st.write(niftyrealty['last'][0])
    #     st.write(niftyrealty['variation'][0])
    #     st.write(niftyrealty['percentChange'][0],'%')   
        


    sep_line = '''---'''
    st.markdown(sep_line)
    st.title('''Welcome to Stock Picker''')
    st.subheader('Make your trading and investment decisions here...')
    st.image('market.jpg')
    st.sidebar.subheader('Navigation Panel')
    
    home_c,tv_c = st.columns(2)
    with home_c:
        if st.sidebar.button('Home'):
            st.experimental_rerun()
    with tv_c:
        st.subheader('Watch TV')   
        tv = st.selectbox('Select Channel',['Select','Zee Business','CNBC Awaaz'])
        if tv  == 'Zee Business' :
            st.video('https://www.youtube.com/watch?v=OoV_YUswOIA')
        if tv == 'CNBC Awaaz':
            st.video('https://www.youtube.com/watch?v=A9f3VanegQA')

    st.sidebar.subheader('Search Stock')
    stock = st.sidebar.text_input('Enter Symbol')
    stock = stock.upper()
    init, final = st.sidebar.columns(2)
    init_ = init.date_input('From')
    final_ = final.date_input('To')
    if st.sidebar.button('Get Stock'):
        init_date = init_
        final_date = final_
        history = get_history(stock,init_date,final_date)
        history = history.drop(['Prev Close','Last','VWAP','Turnover','Trades','Deliverable Volume','%Deliverble'],axis=1)
        history1 = history.reset_index()
        st.write('Stock History')
        st.table(history1)
        st.write('View some basic statistical details like percentile, mean, std etc.')
        history = history1.describe()
        st.table(history)
        plt.figure(figsize=(12,8))
        st.line_chart(history1.Close)
    
    st.sidebar.subheader('Stock Screener')
    scanner = st.sidebar.selectbox('Select Stock Scanner',['Select','Outperforming Stock',
    'Underperforming Stock','Volume Gainer','Above 200 DMA and 50 DMA','Prev. Day Stock by %Change(Rise)',
    'Day Stock by %Change(Fall)'],index=0)
    if scanner == 'Outperforming Stock':
        file_read()
        history_day1 = st.number_input('Enter days to analyze stock:',2)
        if st.button('Get Outrperforming Stock'):
            history1 = []
            for day in range(history_day1):
                history1.append(day)
            today_date = date.today()
            init_date = today_date - timedelta(days=history_day1)
            progress_bar()
            sector_chng = []
            for i in sector:
                i = get_history(symbol=i,start=init_date,end=today_date,index=True)
                init_chng = i.head(1)['Close'][0]
                final_chng = i.tail(1)['Close'][0]
                per_chng = np.round(((final_chng - init_chng)/init_chng)*100,2)
                sector_chng.append(per_chng)
            nifty_chng_df = pd.DataFrame({'Nifty50':sector[0:1], '%Chng':sector_chng[0:1]})
            st.write('Index')
            st.table(nifty_chng_df)
            sector_chng_df = pd.DataFrame({'Sectoral Indices':sector[1:], '%Chng':sector_chng[1:]})
            st.write('Sectors list')
            st.table(sector_chng_df)
            max_chng = np.array(sector_chng[1:]).max()
            # min_chng = np.array(sector_chng).min()
            st.write('Outperforming index of nifty')
            bst_perform_index = sector_chng_df.loc[sector_chng_df['%Chng']==max_chng]
            st.table(bst_perform_index)
            bst_perform_index_loc = str(bst_perform_index.iloc[0,0])
            op_sector_stock = []
            if bst_perform_index_loc == 'NIFTY AUTO':
                sec(sect=auto.Symbol)    
            elif bst_perform_index_loc == 'NIFTY BANK':
                sec(sect=bank.Symbol)    
            elif bst_perform_index_loc == 'NIFTY ENERGY':
                sec(sect=energy.Symbol)    
            elif bst_perform_index_loc == 'NIFTY FIN SERVICE':
                sec(sect=fin_serv.Symbol)    
            elif bst_perform_index_loc == 'NIFTY FMCG':
                sec(sect=fmcg.Symbol)    
            elif bst_perform_index_loc == 'NIFTY IT':
                sec(sect=it.Symbol)    
            elif bst_perform_index_loc == 'NIFTY MEDIA':
                sec(sect=media.Symbol)    
            elif bst_perform_index_loc == 'NIFTY METAL':
                sec(sect=metal.Symbol)
            elif bst_perform_index_loc == 'NIFTY PHARMA':
                sec(sect=pharma.Symbol)    
            elif bst_perform_index_loc == 'NIFTY PSU BANK':
                sec(sect=psu_bank.Symbol)
            elif bst_perform_index_loc == 'NIFTY PVT BANK':
                sec(sect=pvt_bank.Symbol)    
            elif bst_perform_index_loc == 'NIFTY REALTY':
                sec(sect=realty.Symbol)
            

    if scanner == 'Underperforming Stock':
        st.subheader('Underperforming Stock from Outperforming Index')
        file_read()
        history_day = st.number_input('Enter days to analyze stock:',2)
        if st.button('Get Underperforming Stock'):
            history = []
            for day in range(history_day):
                history.append(day)
            today_date = date.today()
            init_date = today_date - timedelta(days=history_day)
            progress_bar()
            sector_chng = []

            for i in sector:
                i = get_history(symbol=i,start=init_date,end=today_date,index=True)
                init_chng = i.head(1)['Close'][0]
                final_chng = i.tail(1)['Close'][0]
                per_chng = np.round(((final_chng - init_chng)/init_chng)*100,2)
                sector_chng.append(per_chng)

            nifty_chng_df = pd.DataFrame({'Nifty50':sector[0:1], '%Chng':sector_chng[0:1]})
            st.subheader('Index')
            st.table(nifty_chng_df)
            sector_chng_df = pd.DataFrame({'Sectoral Indices':sector[1:], '%Chng':sector_chng[1:]})
            st.subheader('Sectors list')
            st.table(sector_chng_df)
            min_chng = np.array(sector_chng[1:]).min()

            # min_chng = np.array(sector_chng).min()
            st.subheader('Underperforming index of nifty')
            bst_perform_index = sector_chng_df.loc[sector_chng_df['%Chng']==min_chng]
            st.table(bst_perform_index)

            bst_perform_index_loc = str(bst_perform_index.iloc[0,0])
            op_sector_stock = []
            if bst_perform_index_loc == 'NIFTY AUTO':
                sec_2(sect=auto.Symbol)    
            elif bst_perform_index_loc == 'NIFTY BANK':
                sec_2(sect=bank.Symbol)    
            elif bst_perform_index_loc == 'NIFTY ENERGY':
                sec_2(sect=energy.Symbol)    
            elif bst_perform_index_loc == 'NIFTY FIN SERVICE':
                sec_2(sect=fin_serv.Symbol)    
            elif bst_perform_index_loc == 'NIFTY FMCG':
                sec_2(sect=fmcg.Symbol)    
            elif bst_perform_index_loc == 'NIFTY IT':
                sec_2(sect=it.Symbol)    
            elif bst_perform_index_loc == 'NIFTY MEDIA':
                sec_2(sect=media.Symbol)    
            elif bst_perform_index_loc == 'NIFTY METAL':
                sec_2(sect=metal.Symbol)
            elif bst_perform_index_loc == 'NIFTY PHARMA':
                sec_2(sect=pharma.Symbol)    
            elif bst_perform_index_loc == 'NIFTY PSU BANK':
                sec_2(sect=psu_bank.Symbol)
            elif bst_perform_index_loc == 'NIFTY PVT BANK':
                sec_2(sect=pvt_bank.Symbol)    
            elif bst_perform_index_loc == 'NIFTY REALTY':
                sec_2(sect=realty.Symbol)

    if scanner == 'Volume Gainer':
        st.subheader('Volume Gainer Of All Sectors')
        file_read()
        history_day = st.number_input('Enter days to analyze stock:',2)
        if st.button('Get Volume Gainer'):
            history = []
            for day in range(history_day-1):
                history.append(day)
            today_date = date.today()
            init_date = today_date - timedelta(days=history_day)
            progress_bar()
            stock_ = []
            avg_vol = []
            sector_ = []
            avg_vol_auto=[]
            avg_vol_bank = []
            avg_vol_energy = []
            avg_vol_fin_serv = []
            avg_vol_fmcg = []
            avg_vol_it = []
            avg_vol_media = []
            avg_vol_metal = []
            avg_vol_pharma = []
            avg_vol_psu_bank = []
            avg_vol_pvt_bank = []
            avg_vol_realty = []
            sectors = [auto.Symbol,bank.Symbol,energy.Symbol,fin_serv.Symbol,fmcg.Symbol,it.Symbol,media.Symbol,
                    metal.Symbol,pharma.Symbol,psu_bank.Symbol,pvt_bank.Symbol,realty.Symbol,None]

            lists = [avg_vol_auto,avg_vol_bank,avg_vol_energy,avg_vol_fin_serv,avg_vol_fmcg,avg_vol_it,
                    avg_vol_media,avg_vol_metal,avg_vol_pharma,avg_vol_psu_bank,avg_vol_pvt_bank,avg_vol_realty,None]

            for i in range(len(sector)):
                try:
                    vol(sectors[i],lists[i],i+1)
                except:
                    continue
                finally:
                    continue

            n_df = pd.DataFrame({'Symbol':stock_,'Avg. Volume':avg_vol,'Sector':sector[1:]})
            n_df = n_df.drop_duplicates(subset="Symbol",keep='last')
            n_df = n_df.reset_index()
            n_df = n_df.drop(['index'],axis=1)
            st.subheader('Volume Gainer Stock From Each Sector')
            st.table(n_df)
            arr_vol = np.array(avg_vol).max()
            vol_df = n_df[n_df['Avg. Volume'] == arr_vol]
            st.subheader('Top Volume Gainer')
            st.table(vol_df)
            fig = plt.figure(figsize=(15,8))
            plt.xlabel('Stock')
            plt.ylabel('Volume in Cr.')
            plt.bar(n_df.Symbol,n_df['Avg. Volume'])
            st.pyplot(fig)
            # st.bar_chart(n_df['Avg. Volume'])

    if scanner == 'Above 200 DMA and 50 DMA':
        st.subheader('Stocks above 200 DMA and 50 DMA')
        file_read()
        if st.sidebar.button('Get Stocks'):
            st.write('Please Wait...\nIt takes few minutes')
            all_stock = auto.Symbol.to_list()+bank.Symbol.to_list()+energy.Symbol.to_list()+fin_serv.Symbol.to_list()+fmcg.Symbol.to_list()+it.Symbol.to_list()+media.Symbol.to_list()+metal.Symbol.to_list()+pharma.Symbol.to_list()+psu_bank.Symbol.to_list()+pvt_bank.Symbol.to_list()+realty.Symbol.to_list()
            final_ma = date.today()
            start_ma = final_ma-timedelta(days=330)
            ma_stock = []
            ma_close = []
            ma_ma200 = []
            ma_ma50 = []
            for i in all_stock:
                try:
                    stock_ma = get_history(i,start_ma,final_ma)
                    stock_ma = stock_ma.drop(['Series','Prev Close','VWAP','Last','Turnover','Trades',
                                        'Deliverable Volume','%Deliverble','Open','High','Low','Volume'],axis=1)
                    ma200 = ta.MA(stock_ma.Close,200)
                    ma50 = ta.MA(stock_ma.Close,50)
                    stock_ma['MA_50'] = ma50
                    stock_ma['MA_200'] = ma200
                    stock_ma = stock_ma.dropna().tail(1)
                    stock_in = stock_ma.reset_index()
                    ma_stock.append(stock_in.loc[0,'Symbol'])
                    ma_close.append(stock_in.loc[0,'Close'])
                    ma_ma200.append(stock_in.loc[0,'MA_200'])
                    ma_ma50.append(stock_in.loc[0,'MA_50'])
                finally:
                    continue
            ma_df = pd.DataFrame({'Symbol':ma_stock,'Close':ma_close,'MA_50':ma_ma50,'MA_200':ma_ma200})
            above_ma200_ma50 = ma_df[(ma_df['Close'] > ma_df['MA_50'] ) & (ma_df['Close'] > ma_df['MA_200'])]
            st.table(above_ma200_ma50)

    
    if scanner == 'Prev. Day Stock by %Change(Rise)' :
        st.subheader('Prev. Day Stock by %Change Rise')
        per_high_num = st.number_input('Enter percentage: ',0,20)
        if st.button('Get Desired Stocks'):
            str_head = str(per_high_num)
            i = 1
            check = [False]
            while check[-1] == False:
                date_ = date.today()- timedelta(i)
                try:
                    his = get_price_list(dt=date_)
                    check.append(True)
                except:
                    check.append(False)
                i+=1
            his = his.drop(['SERIES','LAST','PREVCLOSE','TOTTRDVAL','TOTALTRADES','ISIN'],axis=1)
            chng = np.round(((his.CLOSE-his.OPEN)/(his.OPEN))*100,2)
            his['%CHANGE'] = chng
            his = his[['TIMESTAMP','SYMBOL','OPEN','HIGH','LOW','CLOSE','%CHANGE','TOTTRDQTY']]
            per_stk = his[his['%CHANGE'] >= per_high_num]
            per_stk = per_stk.sort_values(by='%CHANGE',ascending=True)
            per_stk = per_stk.reset_index()
            per_stk = per_stk.drop(['index'],axis=1)
            heading_stk = 'Stocks above '+str_head+'% Change'
            st.subheader(heading_stk)
            st.dataframe(per_stk)

    if scanner == 'Day Stock by %Change(Fall)':
        st.subheader('Prev. Day Stock by %Change Fall')
        per_high_num = st.number_input('Enter percentage: ',-20,0)
        if st.button('Get Desired Stocks'):
            str_head = str(per_high_num)
            i = 1
            check = [False]
            while check[-1] == False:
                date_ = date.today()- timedelta(i)
                try:
                    his = get_price_list(dt=date_)
                    check.append(True)
                except:
                    check.append(False)
                i+=1
            his = his.drop(['SERIES','LAST','PREVCLOSE','TOTTRDVAL','TOTALTRADES','ISIN'],axis=1)
            chng = np.round(((his.CLOSE-his.OPEN)/(his.OPEN))*100,2)
            his['%CHANGE'] = chng
            his = his[['TIMESTAMP','SYMBOL','OPEN','HIGH','LOW','CLOSE','%CHANGE','TOTTRDQTY']]
            per_stk = his[his['%CHANGE'] <= per_high_num]
            per_stk = per_stk.sort_values(by='%CHANGE',ascending=False)
            per_stk = per_stk.reset_index()
            per_stk = per_stk.drop(['index'],axis=1)
            heading_stk = 'Stocks above '+str_head+'% Change'
            st.subheader(heading_stk)
            st.dataframe(per_stk)



    st.sidebar.subheader('Correlation of Indices')
    sector = ['NIFTY', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG',
      'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 'NIFTY PVT BANK', 'NIFTY REALTY']
    days_cor = st.sidebar.number_input('Enter days:',30)
    final_date_cor = date.today()
    init_date_cor = final_date_cor - timedelta(days=days_cor)
    if st.sidebar.button('Get Correlation'):
        st.write('Please Wait... It takes few seconds')
        close_cor = []
        for i in sector:
            df_cor = get_history(i,init_date_cor,final_date_cor,index=True)
            df_cor[i] = df_cor['Close']
            close_cor.append(df_cor['Close'])
        df_cor_ = pd.DataFrame({'NIFTY':close_cor[0],'NIFTY AUTO':close_cor[1],'NIFTY BANK':close_cor[2],'NIFTY ENERGY':close_cor[3],'NIFTY FIN SERVICE':close_cor[4],
    'NIFTY FMCG':close_cor[5],'NIFTY IT':close_cor[6],'NIFTY MEDIA':close_cor[7],'NIFTY METAL':close_cor[8],
    'NIFTY PHARMA':close_cor[9],'NIFTY PSU BANK':close_cor[10],'NIFTY PVT BANK':close_cor[11],'NIFTY REALTY':close_cor[12],})
        returns = df_cor_.pct_change()
        returns = returns*100
        corelation = returns.corr()
        lst = np.arange(13)
        fig, ax = plt.subplots(figsize=(15,15))
        hmap = ax.imshow(corelation,aspect='auto', cmap=plt.cm.RdBu,alpha=0.7)
        fig.colorbar(hmap)
        ax.set_xticks(lst,sector)
        ax.set_yticks(lst,sector)
        plt.setp(ax.get_xticklabels(), ha="right",rotation=45, rotation_mode="anchor")
        for i in range(len(sector)):
            for j in range(len(sector)):
                ax.text(i,j,np.round(corelation.iloc[i,j],2),ha='center',va='center')

        fig.tight_layout()
        # plt.show()
        st.subheader('Correlation of Indices')
        st.pyplot(fig)
    


    st.sidebar.subheader('Intraday Adv/Dec')
    dict_read()
    if st.sidebar.button('OK'):
        sec_key = sec_dic[sector_adv_dec]
        bank = nse.get_indices(sec_key)
        total = []
        bank_advance = bank.advances[0]
        bank_advance = int(bank_advance)
        total.append(bank_advance)
        bank_decline = bank.declines[0]
        bank_decline = int(bank_decline)
        total.append(bank_decline)
        total = np.array(total)
        lst= ['ADVANCE','DECLINE']
        color = ['limegreen','indianred']
        plt.figure(figsize=(5,5))
        def absolute_value(val):
            a  = np.round(val/100.*total.sum(), 0)
            return a
        fig = plt.figure(figsize=(5,5))
        plt.pie(total, labels=lst, autopct=absolute_value,colors=color)
        st.subheader(sector_adv_dec)
        st.pyplot(fig)

    st.sidebar.subheader('Intraday Top Gainers')
    sector_adv_dec_tg = st.sidebar.selectbox('select sector',['NIFTY', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG','NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 
    'NIFTY REALTY', 'NIFTY PVT BANK','NIFTY FNO'])
    sec_dic_tg = {'NIFTY':IndexSymbol.Nifty50, 'NIFTY AUTO':IndexSymbol.NiftyAuto, 
    'NIFTY BANK':IndexSymbol.NiftyBank, 'NIFTY ENERGY':IndexSymbol.NiftyEnergy, 
    'NIFTY FIN SERVICE':IndexSymbol.NiftyFinService, 'NIFTY FMCG':IndexSymbol.NiftyFmcg,
    'NIFTY IT':IndexSymbol.NiftyIt, 'NIFTY MEDIA':IndexSymbol.NiftyMedia, 'NIFTY METAL':IndexSymbol.NiftyMetal, 'NIFTY PHARMA':IndexSymbol.NiftyPharma, 'NIFTY PSU BANK':IndexSymbol.NiftyPsuBank,
    'NIFTY PVT BANK':IndexSymbol.NiftyPvtBank,'NIFTY REALTY':IndexSymbol.NiftyRealty,'NIFTY FNO':IndexSymbol.FnO}
    if st.sidebar.button('Get Top Gainers'):
        sec_key_tg = sec_dic_tg[sector_adv_dec_tg]
        top_gainer = nse.top_gainers(index=sec_key_tg)
        top_gainer = top_gainer.drop(['priority','identifier','previousClose','ffmc','series'],axis=1)
        top_gainer = top_gainer.reset_index()
        top_gainer.rename(columns={'symbol':'Symbol','open':'Open','dayHigh':'Day High','dayLow':'Day Low','lastPrice':'LTP','change':'Change','pChange':'%Change','totalTradedVolume':'Volume'})
        st.subheader('Top Gainers from')
        st.table(top_gainer)

    st.sidebar.subheader('Intraday Top Losers')
    sector_adv_dec_tl = st.sidebar.selectbox('select sector',['NIFTY', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG','NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 
    'NIFTY REALTY', 'NIFTY PVT BANK','NIFTY FNO','NIFTY MIDCAP 50'])
    sec_dic_tl = {'NIFTY':IndexSymbol.Nifty50, 'NIFTY AUTO':IndexSymbol.NiftyAuto, 
    'NIFTY BANK':IndexSymbol.NiftyBank, 'NIFTY ENERGY':IndexSymbol.NiftyEnergy, 
    'NIFTY FIN SERVICE':IndexSymbol.NiftyFinService, 'NIFTY FMCG':IndexSymbol.NiftyFmcg,
    'NIFTY IT':IndexSymbol.NiftyIt, 'NIFTY MEDIA':IndexSymbol.NiftyMedia, 'NIFTY METAL':IndexSymbol.NiftyMetal, 'NIFTY PHARMA':IndexSymbol.NiftyPharma, 'NIFTY PSU BANK':IndexSymbol.NiftyPsuBank,
    'NIFTY PVT BANK':IndexSymbol.NiftyPvtBank,'NIFTY REALTY':IndexSymbol.NiftyRealty,'NIFTY FNO':IndexSymbol.FnO,
    'NIFTY MIDCAP 50':IndexSymbol.NiftyMidcap50}
    if st.sidebar.button('Get Top Losers'):
        st.write('Sector',sector_adv_dec_tl)
        sec_key_tl = sec_dic_tg[sector_adv_dec_tl]
        top_loser = nse.top_losers(index=sec_key_tl)
        top_loser = top_loser.drop(['priority','identifier','previousClose','ffmc','series'],axis=1)
        
        top_loser = top_loser.rename(columns={'symbol':'Symbol','open':'Open','dayHigh':'Day High',
        'dayLow':'Day Low','lastPrice':'LTP','change':'Change','pChange':'%Change','totalTradedVolume':'Volume'})
        # top_loser = top_loser.drop([sector_adv_dec_tl],inplace=True,axis=0)
        top_loser = top_loser.reset_index()
        st.table(top_loser)
        
        