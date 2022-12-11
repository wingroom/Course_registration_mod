import tabula
import Course_registration_FILE as FILE

tabula.convert_into('setup\seme1.pdf', 'setup\seme.csv', output_format='csv', pages='all')

