def hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x

def compute_cost(x, y, theta0, theta1):
    m = len(x)
    total_error = 0
    for i in range(m):
        prediction = hypothesis(x[i], theta0, theta1)
        total_error += (prediction - y[i]) ** 2
    return total_error / (2 * m)

def gradient_descent(x, y, theta0, theta1, alpha, iterations):
    m = len(x)
    for _ in range(iterations):
        sum_error0 = 0
        sum_error1 = 0
        for i in range(m):
            error = hypothesis(x[i], theta0, theta1) - y[i]
            sum_error0 += error
            sum_error1 += error * x[i]
        theta0 = alpha * (1/m) * sum_error0
        theta1 = alpha * (1/m) * sum_error1
    return theta0, theta1
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Initial parameters
theta0 = 0
theta1 = 0
alpha = 0.01
iterations = 1000

# Train the model
theta0, theta1 = gradient_descent(x, y, theta0, theta1, alpha, iterations)

# Final cost
cost = compute_cost(x, y, theta0, theta1)
print(f"Final Cost: {cost}, theta0: {theta0}, theta1: {theta1}")
