"""

class rsa
    functions:
        is_prime - checking number 
	rsa_c - return public and private key
	code - encryption file
	decode - decoding function code


"""

import random as rand
class rsa():
    def is_Prime(self,n):
        s = 0
        d = n-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == n-1)
     
        def trial_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True  
     
        for i in range(20): 
            a = rand.randrange(2, n)
            if trial_composite(a):
                return False
     
        return True  
    def rsa_c(self):
        
        p=int(rand.uniform(10000000,100000000))
    
        while True:
            p+=1
            if self.is_Prime(p):
                break

        q=int(rand.uniform(10000000,100000000)) 
        while True:
            q+=1
            if self.is_Prime(q):
                break
        
        n=q*p
        euler =(q-1)*(p-1)
        
        for x in range(10,n-1):
            a=x
            b=euler
            while b:
                a,b=b,a%b
            if a == 1:
                e=x
                break
                
        #print(n,euler,e)
        
        for i in range(2,n): 
            x = 1 + i*euler 
            if x % e == 0: 
                d = int(x/e) 
                break
        
        
        
        private=[n,e]
        public=[n,d]
        
        file = open("private.txt", "w+") 
        file.write(str(n)+" "+str(e))
        file.close()

        file = open("public.txt", "w+") 
        file.write(str(n)+" "+str(d))
        file.close()
        
        return [private,public]


    def code(self,plik,priv):

        """algorithm with modular division"""
        
        filep= open(priv,"r")
        priv= filep.read()
        priv= priv.split(" ")
        filep.close()

        file = open(plik, "r") 
        text= file.read() 
        file.close()
        back=""
        
        c=int(priv[1])
        n=int(priv[0])
        b=bin(c)
        b=b[::-1]    
        for x in text:
            t=ord(x)
            zw=[]
            for x in range(0,len(b)-2):
                if b[x]=="1":
                    zw.append(t)
                #print(b[x])
                #print(t)
                t=((t)**2)%n

            y=1
            for k in zw:
                y*=k

            y=(y%n) 
            back=back+" "+str(y)
            
        file= open(plik,"w+")
        file.write(back)
        file.close()
        return True
            



    def decode(self,d_file,public,to_file=""): 

        """algorithm with modular division"""
        
        filep= open(public,"r")
        public= filep.read()
        public=public.split(" ")
        filep.close()
        
        file = open(d_file, "r") 
        text= file.read() 
        file.close()

        
        back=text
        back=back.split(" ")
          
        b=bin(int(public[1]))
        b=b[::-1]
        p1=int(public[0])
        
        translate=""
        for x in back[1:]:
            
            byte = x
            m=1
            zw=[]
            byte=int(byte)%p1
            for x in range(0,len(b)-2):
                if b[x]=="1":
                    zw.append(int(byte))  
                byte=(int(byte)**2)%p1
                      
                      
            for k in zw:
                m*=k

            m=(m%p1)        
            
            m=chr(m)
            translate=translate+str(m)

            
        if to_file =="":
            file = open(d_file, "w+") 
            file.write(translate)
        else:
            file = open(to_file, "w+") 
            file.write(translate)   
        file.close()
        return True
    
	
r=rsa()
klucz=r.rsa_c()

#r.code("tocode.txt",klucz[0])

#r.decode("tocode.txt",klucz[1])

r.code("tocode.txt","private.txt")

r.decode("tocode.txt","public.txt")
