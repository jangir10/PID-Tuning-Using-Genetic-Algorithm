# app.py
from flask import Flask, request, jsonify, render_template
import numpy as np
from scipy import signal
import control as ctrl
from geneticalgorithm import geneticalgorithm as ga

app = Flask(__name__)

def calculate_pid_parameters(num_coeff, den_coeff):
    """
    Calculate PID parameters from transfer function coefficients
    with improved error handling and pole calculation
    """
    try:
        # Create transfer function
        sys = ctrl.TransferFunction(num_coeff, den_coeff)
        
        # Get poles of the system using poles() instead of pole()
        poles = sys.poles()
        
        # If we have complex poles, use the dominant pair
        if len(poles) > 0:
            t = np.arange(0, 30.01, 0.01)
            r = np.ones(len(t))
            def compute_ITAE(K, plant_tf, r, t):
            # Simulate the closed-loop system
                controller_tf = ctrl.TransferFunction([K[2],K[0],K[1]], [1,0])
                closed_loop_tf = ctrl.feedback(ctrl.series(controller_tf, plant_tf), 1)
                t_sim, y = ctrl.step_response(closed_loop_tf, T=t)

                # Compute ITAE criteria
                error = y - r
                ITAE_value = np.trapz(t_sim * np.abs(error), t_sim)
                return ITAE_value
            
            def fitness_function(K):
                # print(len(X))
                objective = compute_ITAE(K,sys, r, t)
                return objective
            
            varbound = np.array([[0, 20.09],[0, 5],[0,5]])
            algorithm_param = {'max_num_iteration': 50,\
                   'population_size':10,\
                   'mutation_probability':0.3,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 1,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}
            optimizer = ga(function=fitness_function, dimension=3, variable_type='real', variable_boundaries=varbound, algorithm_parameters=algorithm_param)
            optimizer.run()
            best_solution = optimizer.output_dict
            best_Params = best_solution['variable']
            Kp = best_Params[0]
            Ki = best_Params[1]
            Kd = best_Params[2]
            return {
                'Kp': float(round(Kp, 3)),
                'Ki': float(round(Ki, 3)),
                'Kd': float(round(Kd, 3))
            }
        else:
            raise ValueError("No poles found in the system")
            
    except Exception as e:
        raise Exception(f"Error in PID calculation: {str(e)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num_str = data['numerator']
        den_str = data['denominator']
        
        # Convert string inputs to coefficient lists
        num_coeff = [float(x.strip()) for x in num_str.split(',')]
        den_coeff = [float(x.strip()) for x in den_str.split(',')]
        
        # Validate inputs
        if len(num_coeff) == 0 or len(den_coeff) == 0:
            return jsonify({'success': False, 'error': 'Coefficients cannot be empty'})
            
        if den_coeff[0] == 0:
            return jsonify({'success': False, 'error': 'Leading denominator coefficient cannot be zero'})
        
        pid_params = calculate_pid_parameters(num_coeff, den_coeff)
        return jsonify({'success': True, 'parameters': pid_params})
        
    except ValueError as ve:
        return jsonify({'success': False, 'error': f'Invalid input: {str(ve)}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)