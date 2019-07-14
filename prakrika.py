from flask import Flask, jsonify, request, abort


app = Flask(__name__)

Yachmenev = [
    {
        'id': 1,
        'subject': u'vichmat',
        'rating': u'4'
    },
    {
        'id': 2,
        'subject': u'Bondarb',
        'rating': u'4'
    },
    {
        'id': 3,
        'subject': u'OS',
        'rating': u'5'
    },
    {
        'id': 4,
        'subject': u'EVM',
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

    
if __name__ == '__main__':
    app.run(debug=True)
    


