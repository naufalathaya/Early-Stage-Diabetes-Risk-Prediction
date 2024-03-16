from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    age = float(request.form['age'])
    gender = float(request.form['gender'])
    polyuria = float(request.form['polyuria'])
    polydipsia = float(request.form['polydipsia'])
    sudden_weight_loss = float(request.form['sudden_weight_loss'])
    weakness = float(request.form['weakness'])
    polyphagia = float(request.form['polyphagia'])
    genital_thrush = float(request.form['genital_thrush'])
    visual_blurring = float(request.form['visual_blurring'])
    itching = float(request.form['itching'])
    irritability = float(request.form['irritability'])
    delayed_healing = float(request.form['delayed_healing'])
    partial_paresis = float(request.form['partial_paresis'])
    muscle_stiffness = float(request.form['muscle_stiffness'])
    alopecia = float(request.form['alopecia'])
    obesity = float(request.form['obesity'])
    # Make prediction
    prediction = model.predict([[age, gender, polyuria, polydipsia, sudden_weight_loss, weakness, polyphagia, genital_thrush, visual_blurring, itching, irritability,
                                 delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity]])[0]
    # Map prediction result to text
    if prediction == 1:
        result = 'Positive'
    else:
        result = 'Negative'
    # Return the result
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
