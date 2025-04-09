from flask import Flask

app = Flask(__name__)
@app.route('/summa/<int:luku>')
def summaa(luku):
    if luku % luku == 0 and luku % 1 == 0:
        for i in range(2, luku):
            luku % i
            if luku % i == 0:
                summa = {
                    'Number': luku,
                    'isPrime': False
                }
                break

            elif i == luku - 1 and luku % i != 0:
                summa = {
                    'Number': luku,
                    'isPrime': True
                }
                break

    else:
        summa = {
            'Number': luku,
            'isPrime': True
        }
    return str(summa)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)