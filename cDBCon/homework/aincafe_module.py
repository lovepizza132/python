import cx_Oracle as oci

class aincafe_module:
    @staticmethod
    def order(orderList, price, payment):

        conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")
        cursor = conn.cursor()

        # 구매리스트 DB 입력
        sql1 = '''
                    INSERT INTO purchaselist
                    (purchaselist_id, purchaselist_date, purchaselist_payment)
                    values(seq_purchaselist_pk.nextval, sysdate, :payment)
                '''
        cursor.execute(sql1,(payment,))

        # 구매상품 리스트 DB 입력
        for item in orderList:
            purchase_quantity = orderList[item]
            purchase_price = price[item]

            sql2 = '''
                   INSERT INTO purchase
                    (purchase_id, purchaselist_id, purchase_name, purchase_quantity, purchase_price)
                    values(seq_purchase_pk.nextval, seq_purchaselist_pk.currval, :item, :purchase_quantity, :purchase_price) 
            '''
            cursor.execute(sql2,(item, purchase_quantity, purchase_price))


        # 구매리스트 id 제공(환불을 위해)
        sql3 = '''
                SELECT purchaselist_id from purchaselist where buylist_id=seq_purchaselist_pk.currval
        '''
        cursor.execute(sql3)
        datas = cursor.fetchall()

        return datas

        conn.commit()
        cursor.close()
        conn.close()