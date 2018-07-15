# ICML-2017 proceedings: "bibtex to RIS" in order to import to Endnote X8.
#--code--:utf-8

import os

def bib_2_ris( bib_file ):
	sub_dir=bib_file.split(os.sep)[-2]
	#print('sub_dir:',sub_dir)
	label_dir_path=os.path.split(bib_file)[0]
	ris_result=os.path.join(label_dir_path, 'ris_result.txt')
	with open(bib_file, 'rb') as file_in:
		with open(ris_result,'wb') as file_out:
			line =file_in.readline()
			while line:
				line = bytes.decode(line.strip())
				if line=='':
					line = file_in.readline()
					continue
				#print(line)
				#line_str=''
				if line.strip().startswith('@'):
					line_arr = line.split('{')
					#label=os.path.join(label_dir_path,line_arr[1][:-1])
					label ='internal-pdf://../'+os.path.join(sub_dir , line_arr[1][:-1])
					line_str='LB  - '+ line_arr[1][:-1]
					file_out.write(str.encode(line_str+'\n','utf-8'))
				if line.strip().startswith('@InProceedings'):
					line_str='TY  - '+'CONF'
				else:
					line_arr = line.strip().strip('\t').split('=')
					if len(line_arr) < 2:
						if line.strip().startswith('}'):
							line_str='L1  - '+ label +'.pdf'+'\n'
							line_str +='L1  - '+ label+'-supp'+'.pdf'+'\n'
							line_str +='ER  -  \n'
							file_out.write(str.encode(line_str+'\n','utf-8'))
						line = file_in.readline()
						continue
					for i in range(len(line_arr[1])):
						#print('i=',i)
						if line_arr[1][i]=='{':
							value=line_arr[1][i+1:-2]
							break
					#if 'title ='in line:
					if line.strip().startswith('title = '):
						#line_arr = line.split('{')
						line_str='TI  - '+value
					if line.strip().startswith('author = '):
						#line_arr = line.split('{')
						line_str='AU  - '+value
					if line.strip().startswith('abstract = '):
						#line_arr = line.split('{')
						line_str='AB  - '+value
					if line.strip().startswith('pages = '):
						line_str='PA  - '+value
					if line.strip().startswith('year = '):
						line_str='PY  - '+value
					if line.strip().startswith('url = '):
						line_str='UR  - '+value
					if line.strip().startswith('doi = '):
						line_str='DO  - '+value
					if line.strip().startswith('volume = '):
						line_str='VL  - '+value
					if line.strip().startswith('publisher = '):
						line_str='PB  - '+value
					if line.strip().startswith('editor = '):
						line_str='A2  - '+value
					if line.strip().startswith('series = '):
						line_str='T3  - '+value
					if line.strip().startswith('booktitle = '):
						line_str='C3  - '+value
					if line.strip().startswith('address = '):
						line_str='CY  - '+value
					if line.strip().startswith('month = '):
						line_str='DA  - '+value
					if line.strip().startswith('pdf = '):
						line_str='OP  - '+value
						#print("==",line_str, line_arr[1])
				#print(line_str)
				file_out.write(str.encode(line_str+'\n','utf-8'))

				line =file_in.readline()


if __name__=='__main__':
	bib_file='bibliography.bib'
	bib_file = 'D:/EndNoteX8/Library-Data/AI-and-Network-20180314.Data/ICML-2017/bibliography.bib'
	bib_file=os.path.abspath(bib_file)

	print(bib_file)
	bib_2_ris(bib_file)
	print('Finished!')






