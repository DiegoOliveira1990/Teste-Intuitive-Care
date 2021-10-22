import tabula

file = "padrao_tiss_componente_organizacional_202108.pdf"

table1 = tabula.read_pdf(file, pages=108, multiple_tables=True)
# convert PDF into CSV file
tabula.convert_into(file, "Teste_Intuitive_Care_Diego.csv",
                    output_format="csv", pages=(108, 109, 110, 111, 112, 113, 114))
