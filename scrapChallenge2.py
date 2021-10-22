import tabula
import zipfile

file = "padrao_tiss_componente_organizacional_202108.pdf"

table1 = tabula.read_pdf(file, pages=108, multiple_tables=True)
# convert PDF into CSV file
tabula.convert_into(file, "Quadro30.csv",
                    output_format="csv", pages=(108))
tabula.convert_into(file, "Quadro31e32.csv",
                    output_format="csv", pages=(109,110,111,112,113,114))

z = zipfile.ZipFile('Teste_Intuitive_Care(Diego).zip', 'w', zipfile.ZIP_DEFLATED)
z.write('Quadro30.csv')
z.write('Quadro31e32.csv')
z.close()
