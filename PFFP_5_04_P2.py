import numpy

class DerivativePricer:
    def __init__(self):
        pass
    def get_price(self):
        pass
    def absolute_price(self):
        price = self.get_price()
        return abs(price)
                                                    #dependency injection
class OprionPricingTreeModel(DerivativePricer):
    '''
    Short description of what we want to achieve
    
    Attributes:
        ---
        
        S0: float
            initial stock price
        T: int
            number of periods
        delta_T: float
            the increment
        K : float
            strike price
        r : float
            risk-free rate
        sigma : float
            volatility
        option_type : str
            call or put
        multiplier: float
            used to multiply given fucntion this number. One can change it dynamically
       # u : float
       #     going up
       # d : float
       #     going down

    Method:
        ---
        parametrisation(self):
            CRR, Jarrow-Rudd, but could be sth else
    '''
    def __init__(self, S0: float, T: int, delta_T: float, 
                 K: float, r: float, sigma: float, 
                 option_type: str, method, multiplier: float):
        self.S0=S0
        self.T=T
        self.delta_T=delta_T
        self.K=K
        self.r=r
        self.sigma=sigma
        self.option_type=option_type
        self.method=method
        self.multiplier = multiplier      #MUSI BYC PPRZED COMPUTE PARAM, BO TAM TEGO UZYWA!
        self.u, self.d = self.compute_parametrisation() 
        #self.multiplier = multiplier               WAZNA KOLEJNOSC TU NIE MOZE BYC, BO JESZCZE NIE ZNA!!
        super().__init__()



#naucz sie specyfikacji z czego co inheratitujemy!!

    def compute_crr_param(self):
        u = numpy.exp(self.sigma*self.delta_T)
        d = 1/u
        return u,d
    def compute_jr_param(self):
        pass
    def compute_parametrisation(self) -> (float, float):
        if self.method == 'CRR':
            return self.compute_crr_param()
        elif self.method == 'JR':
            return self.compute_jr_param()
        else: 
            return self.method(self.multiplier) #jezeli bez argumentu to na koniec samo self, bo to funkcja!
        
    def get_price(self, model):
        return 5
    
def new_param_method(obj):  #przyjmuje 1 argument, wiec w compute param musi byc self, lub self.sth
    return 1.5*obj, 0.5*obj
    
my_model = OprionPricingTreeModel(S0= 1000, T=5, delta_T=0.1, 
             K=105, r=1.1, sigma=1.5, 
             option_type='call', method=new_param_method, multiplier = 3)  
#podaje jako nazwe, nie trzeba podkreslac ze to funkcja

u, d = my_model.compute_parametrisation()
print(u, d)
print(my_model.compute_parametrisation())

my_model = OprionPricingTreeModel(S0= 1000, T=5, delta_T=0.1, 
             K=105, r=1.1, sigma=1.5, 
             option_type='call', method=new_param_method, multiplier = 3) 



#napisz jakis swoj kod jak bedziesz czas mial, naucz sie filter i map duzo mocniej!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
