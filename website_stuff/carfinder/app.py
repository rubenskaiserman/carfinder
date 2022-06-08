from flask import Flask, request, render_template
import psycopg

app = Flask(__name__)

def json_parse(data: list, cur) -> list:
    response = []
    for result in data:
        i = 0
        json_data = dict()
        for column in cur.description:
            json_data[column.name] = result[i]
            i += 1
        response.append(json_data)
    return response

@app.route('/', methods=["GET", "POST"])
def index():
    columns = [
        'marca', 'modelo', 'mod', 'body_type', 'portas', 'bancos', 'bagagem', 'combustivel', 'sistema_combustivel',
        'tipo_motor', 'posicao_motor', 'capacidade_motor', 'cylinders', 'power_out', 'aceleracao', 'velocidade_max',
        'rodas_motrizes', 'tipo_direcao', 'gear_box', 'comprimento', 'largura', 'altura', 'peso', 'wheel_base', 
        'suspencao_frontal', 'suspencao_traseira', 'freios_frontais', 'freios_traseiros', 'pneus_frontais', 
        'pneus_traseiros', 'fuel_urban', 'fuel_extra_urban', 'fuel_combined', 'volume_tanque'
        ]

    with psycopg.connect("dbname=car_search user=usuario password='batatinha123'") as conn:
        with conn.cursor() as cur:
            GET = request.args.get("q")
            if GET != None:
                GET = GET.lower()
                has_result = False
                for column in columns:
                    try:
                        cur.execute(f"SELECT id, marca, modelo, mod, img FROM cars WHERE {column} LIKE '%{GET}%'")
                        result = json_parse(cur.fetchall(), cur)
                        if result != []:
                            has_result = True
                            break
                    except:
                        pass
                if has_result:
                    return render_template("index.html", result=result)
                else:
                    return render_template("index.html", result="Lasanha")
            else:
                return render_template("index.html", result=False)

@app.route('/car')
def car():
    with psycopg.connect("dbname=car_search user=usuario password='batatinha123'") as conn:
        with conn.cursor() as cur:
            try:
                GET = request.args.get('car')
                cur.execute(f"SELECT * FROM cars WHERE id='{GET}'")
                response = json_parse(cur.fetchall(), cur)
                return render_template("car.html", response=response[0])
            except:
                return render_template("error404.html")

    