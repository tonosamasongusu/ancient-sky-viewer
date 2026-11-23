# 夜空ビューアのビルド: template.html + skydata.js + milkyway-data.js -> sky.html
import pathlib
d = pathlib.Path(__file__).parent
t = (d / 'template.html').read_text()
t = t.replace('/*SKYDATA*/', (d / 'skydata.js').read_text())
t = t.replace('/*MWDATA*/', (d / 'milkyway-data.js').read_text())
t = t.replace('/*COMETS*/', (d / 'comets-data.js').read_text())
(d / 'sky.html').write_text(t)
print('built sky.html', len(t), 'bytes')
