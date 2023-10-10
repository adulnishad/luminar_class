

# ---variable length arugument method----- 

#def  product(*args):
    #res=1
   # for n in args:
  #      res*=n
 #   print(res)


#product(1,2,3,4)
#product(10,20)

#def greetings(**kwrgs):
 #   print(f"hello {kwrgs.get('msg')} app user {kwrgs.get('user_name')}")


#greetings(msg="good morning",user_name="ab")


#hello user vijay you order 123b ucb shirt is ready to delivery


def dispatch_order(**kwargs):
    item=kwargs.get("item")
    code=kwargs.get("code")
    status=kwargs.get("status")
    name=kwargs.get("name")
    print(f"hello user {name} your order {code}{item} is redy to {status}")
dispatch_order(item="ucb shirt",code="123abc",status="delivery",name="vijay")



#-----method overloding------

class claculator:

    def add(self,n1,n2):
        print(n1+n2)

    def add(self, n1,n2,n3):
        print(n1+n2+n3)

obj=claculator()
obj.add(10,20,30)