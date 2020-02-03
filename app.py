from flask import Flask, render_template, request

from predict import predict

app = Flask(__name__)

symptoms_list = []
predicted_diseases = []


# CHECKING WHETHER ALL THE MODELS HAVE BEEN SUCCESSFULLY IMPORTED OR NOT


@app.route('/', methods=['GET', 'POST'])
def home():
    symptoms_list.clear()
    if request.method == 'GET':
        current_symptom = request.args.get('user-symptoms')
        if current_symptom and current_symptom not in symptoms_list:
            symptoms_list.append(current_symptom)
        discarded_symptom = request.args.get('delete-symptom')
        if discarded_symptom:
            symptoms_list.remove(discarded_symptom)
        return render_template('index.html', symptoms=symptoms_list)
    elif request.method == 'POST':
        if len(symptoms_list) < 5:
            list_underflow = "Please enter at least 5 symptoms for proper prediction"
            return render_template('index.html', symptoms=symptoms_list, list_underflow=list_underflow)
        else:
            predicted_diseases = predict(symptoms_list=symptoms_list)
            return render_template('index.html', symptoms_list=symptoms_list, predicted_diseases=predicted_diseases)
    return render_template('index.html', symptoms_list=symptoms_list)
    #  when the search button is invoked

    #  context = {
    #         'symptoms': symptoms
    # }
    # if len(symptoms) < 5:
    #     list_underflow = "Please enter at least 5 symptoms for proper prediction"
    #     context['list_underflow'] = list_underflow
    # else:
    #     predicted_diseases = process_symptoms(symptoms)
    #     # symptoms.clear()
    #     context['predicted_diseases'] = predicted_diseases
    # return render(request, 'symptoms/index.html', context=context)



if __name__ == '__main__':
    app.run(debug=True)
