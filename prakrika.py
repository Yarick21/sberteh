from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
