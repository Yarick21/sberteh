from flask import Flask, jsonify, request, abort


app = Flask(__name__)

Yachmenev = [
    {
        'id': 1,
        'subject': u'Computational Mathematics',
        'rating': u'4'
    },
    {
        'id': 2,
        'subject': u'Electrical Engineering',
        'rating': u'4'
    },
    {
        'id': 3,
        'subject': u'OS',
        'rating': u'5'
    },
    {
        'id': 4,
        'subject': u'EVM&LU',
        'rating': u'5'
    }
]

@app.route('/api/Yachmenev', methods=['GET'])
def get_Yachmenev():
    return jsonify({'Yachmenev': Yachmenev})

@app.route('/api/Yachmenev/<int:nomer>', methods=['GET'])
def get2_Yachmenev(nomer):
    return jsonify({'Yachmenev': Yachmenev[nomer-1]})

@app.route('/api/Yachmenev/<int:nomer>', methods=['DELETE'])
def delete_Yachmenev(nomer):
    Yachmenev.remove(Yachmenev[nomer])
    return jsonify({'result': True})

@app.route('/api/Yachmenev/<int:id>', methods=['PUT'])
def update_task(id):
    Yachmenev[id-1]['rating'] = request.json.get('rating')
    Yachmenev[id-1]['subject'] = request.json.get('subject')
    return jsonify({'Yachmenev/'+str(id): Yachmenev[id-1]})

    
if __name__ == '__main__':
    app.run(debug=True)
    


