import numpy as np
import pandas as pd

class evaluate:

    def metrics_recall(user_recall_items_dict, trn_last_click_df, topk=5):
        last_click_item_dict = dict(zip(trn_last_click_df['user_id'], trn_last_click_df['click_article_id']))
        user_num = len(user_recall_items_dict)
        
        #ghjgjhkgjkhlkjhlkjhkj
        #khkjhkljhjkl

        for k in range(10, topk+1, 10):
            hit_num = 0
            recall_num=user_num*topk
            nmrr=0

            for user, item_list in user_recall_items_dict.items():
                # 获取前k个召回的结果
                tmp_recall_items = [x[0] for x in user_recall_items_dict[user][:k]]
                if last_click_item_dict[user] in set(tmp_recall_items):
                    hit_num += 1
                    ind=tmp_recall_items.index(last_click_item_dict[user])+1
                    nmrr+=round(1.0 / ind, 5)

                
            hit_rate = round(hit_num * 1.0 / user_num, 5)
            precision = round(hit_num * 1.0 / recall_num, 5)
            recall = round(hit_num * 1.0 / user_num, 5)
            if hit_rate==0:
                f1=0
            else:
                f1 = round(recall * precision * 2.0 / ( recall + precision ), 5)
            mrr = round(nmrr * 1.0 / recall_num, 5)
            print(' topk: ', k, ' : ', 'hit_num: ', hit_num, 'hit_rate: ', hit_rate, 'user_num : ', user_num,'precision:',precision,'recall:',recall,'f1:',f1,'mrr:',mrr)
