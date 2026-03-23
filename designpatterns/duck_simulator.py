from strategy_duck import Duck

class DuckSimulator:
    
    def simulate(self, duck : Duck):
        self.__fly_n_times(duck, 2)
        duck.quack()
        self.__fly_n_times(duck, 3)
        
    def __fly_n_times(duck : Duck, n_times : int):
        for _ in range(n_times):
            duck.fly()
        
    