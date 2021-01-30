from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def main_page():
	return "Main Page"

@app.route('/embedded')
def embedded():
	return render_template('embedded.html')

@app.route('/loadscript')
def loadscript():
	return render_template('loadscript.html')

@app.route('/compvis')
def compvis():
	return render_template('compvis.html', pdb_file='6ij6.pdb', pdb_csv='6ij6.csv')


@app.route('/compvis/<pdb_id>')
def dynamic_compvis(pdb_id):
	
	pdb_id   = pdb_id.lower()
	pdb_file = pdb_id + ".pdb"
	pdb_csv  = pdb_id + ".csv"
	return render_template('compvis.html', pdb_file=pdb_file, pdb_csv=pdb_csv)

@app.route('/compvis2')
def compvis2():
	return render_template('compvis2.html', pdb_file='6ij6.pdb', pdb_csv='6ij6.csv')


@app.route('/compvis2/<pdb_id>')
def dynamic_compvis2(pdb_id):
	
	pdb_id   = pdb_id.lower()
	pdb_file = pdb_id + ".pdb"
	pdb_csv  = pdb_id + ".csv"
	return render_template('compvis2.html', pdb_file=pdb_file, pdb_csv=pdb_csv)


if __name__=="__main__":

	app.run(debug=True)


