from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import matplotlib.pyplot as plt
from flask import send_file
from sklearn import linear_model
import io

app = Flask(__name__)


@app.route('/')
def get_input():
    """Return the webpage of input form."""
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def draw_distribution():
    param_list_x = ['X_1','X_2','X_3','X_4', 'X_5']
    x_list = []
    for param in param_list_x:
        x_list.append(float(request.args.get(param)))
    
    param_list_y = ['Y_1','Y_2','Y_3','Y_4', 'Y_5']
    y_list = []
    for param in param_list_y:
        y_list.append(float(request.args.get(param)))

   
    x_list = np.array(x_list)
    x_list = np.reshape(x_list, [-1, 1])
    y_list = np.array(y_list)
    
    # fit the model 
    model = linear_model.LinearRegression().fit(x_list, y_list)
    # plot  
    plt.title("The linear relationship is:y = %fx + %f " %(model.coef_,model.intercept_))
    plt.scatter(x_list, y_list, color="black")
    plt.plot(x_list, model.coef_*x_list +model.intercept_)

   
    img = io.BytesIO()   
    #plt.savefig(img, format='png')
    #plt.close()
    #img.seek(0)

    #plot_url = base64.b64encode(img.getvalue())
    #print(plot_url)
    #return render_template('picture.html', plot_url=plot_url)
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)