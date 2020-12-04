from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def main_page():
	return "Main Page"


@app.route('/compvis')
def compvis():
	return render_template('compvis.html')


@app.route('/compvis/<pdb_id>')
def dynamic_compvis(pdb_id='6ij6'):
	
	pdb_id   = pdb_id.lower()
	pdb_file = pdb_id + ".pdb"
	pdb_csv  = pdb_id + ".csv"
	return render_template('compvis.html', pdb_file=pdb_file, pdb_csv=pdb_csv)


if __name__=="__main__":

	app.run(debug=True)


