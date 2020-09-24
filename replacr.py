import sys, getopt

def main(argv):
   tex_file = ''
   map_file = ''
   help_message = 'replacr.py -t <path to tex file> -m <path to mapping file>'

   # try to parse command line arguments, otherwise quit with help message
   try:
      opts, args = getopt.getopt(argv,"ht:m:",["tex=", "map="])
   except getopt.GetoptError:
      print(help_message)
      sys.exit(2)

   # handle used command line options
   for opt, arg in opts:
      if opt == '-h':
         print(help_message)
         sys.exit()
      elif opt in ("-t", "--tex"):
         tex_file = arg
      elif opt in ("-m", "--map"):
         map_file = arg

   # replace placeholders
   replace(tex_file, map_file)

def replace(tex_file, map_file):
    print('Tex file is:', tex_file)
    print('Mapping file is:', map_file)

    mapping_dict = {}
    # read mapping file and save it in dictionary
    with open(map_file, encoding='utf-8') as mf:
        lines = [line.rstrip() for line in mf]
        for line in lines:
            parts = line.split('=', 1) #splits only by first occurence of =
            mapping_dict[parts[0].strip()] = parts[1]

    # read tex file
    tex_code = ''
    with open(tex_file, encoding='utf-8') as tf:
        tex_code = tf.read()
        tex_code = tex_code.replace(tex_file.split('.')[0], 'new' + tex_file.split('.')[0])
        
    # replace placeholders in tex file
    for key in mapping_dict:    
        tex_code = tex_code.replace('§{' + key + '}', mapping_dict[key])

    # write new tex file
    new_tex_file = 'new' + tex_file
    with open(new_tex_file, 'w', encoding='utf-8') as tf:
        tf.write(tex_code)
        print('Output file:', new_tex_file)

if __name__ == "__main__":
   main(sys.argv[1:])
