import numpy as np

class linear_regressor:
    def __init__(self,num_interation,learning_rate,initial_m,initial_b):
        self.num_interation = num_interation
        self.learning_rate = learning_rate
        self.m = initial_m
        self.b = initial_b

    def compute_gradient(self,data):
        total_gradient_m = 0
        total_gradient_b = 0
        for i in range(len(data)):
            if i > 0:
                x,y=data[i]
                total_gradient_m += 2 * x * (self.predict(x)-y)
                total_gradient_b += 2 * (self.predict(x) - y)
        average_gradient_m = total_gradient_m / float(len(data))
        average_gradient_b = total_gradient_b / float(len(data))
        return average_gradient_m, average_gradient_b


    def train(self,data):
        for i in range(self.num_interation):
            gradient_m, gradient_b = self.compute_gradient(data)
            self.m -= gradient_m * self.learning_rate
            self.b -= gradient_b * self.learning_rate

        


    def predict(self,x):
        return self.m * x + self.b

    def computeMSE(self,data):
        total_SE = 0
        #print(len(data))
        for i in range(len(data)):

            if i>0:
                [x,y]=data[i]
                #print(y)
                #print(data[i])
                predict_y = self.predict(x)
                #print(predict_y)
                tempValue = np.square(y - predict_y)
                total_SE += tempValue
        average_SE =total_SE/ float(len(data))
        return average_SE





def run():
    data=np.genfromtxt('example_data.csv',delimiter=',')
    #print(data.shape)
    #print(data)


    #inilization,define hyper parameter

    num_interation = 1000
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0

    model = linear_regressor(num_interation,learning_rate,initial_m,initial_b)
    
    print('Before training, error is {0}',format(model.computeMSE(data)))

    model.train(data)
    print('After training, error is {0}',format(model.computeMSE(data)))

    print('After training, m is {0}, b is {1}',model.m,model.b)




run()
