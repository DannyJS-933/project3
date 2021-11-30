import os
 
ruta_absoluta = '/Users/dannygarcia/Documents/Python-UCR/Tarea_corta#3/tarea.txt'
 
if os.path.exists(ruta_absoluta) == False:
    file = open(ruta_absoluta, 'x+')
    agregar_texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet lectus ac elit dapibus accumsan sit amet ac leo. Sed nisi est, rutrum et consequat vel, volutpat ut quam. Phasellus non pretium mi. Duis congue eu dui vel vehicula. Maecenas vel suscipit risus, a sagittis augue. Proin cursus nunc at ex accumsan bibendum id nec libero. Phasellus varius pharetra mi, sed bibendum lacus dictum sit amet. Vestibulum a pretium nibh.

                        Duis ornare, purus vel malesuada tristique, diam velit fringilla nulla, ut pharetra dolor mauris ac libero. Aenean nisl ligula, egestas sit amet iaculis et, imperdiet hendrerit ex. Praesent feugiat arcu magna. Ut tellus magna, auctor quis suscipit vitae, faucibus a arcu. Curabitur sagittis odio nec blandit facilisis. Proin ex nulla, iaculis sed bibendum et, mattis et risus. Curabitur eros enim, venenatis non justo eget, bibendum posuere nulla. Aliquam a ullamcorper massa. Quisque consequat justo urna, non pretium arcu mattis non. Donec et accumsan nibh. Mauris volutpat sapien in neque ultricies, non ultricies libero sollicitudin. Sed sit amet libero odio. Morbi ipsum orci, condimentum ac odio at, porttitor viverra nisl. Integer sed magna in mi placerat finibus sed nec lectus.

                        Aliquam erat volutpat. Suspendisse vulputate commodo nisl, non mollis ligula dignissim at. Phasellus sollicitudin nisl eget fermentum tristique. Integer a turpis massa. Phasellus eget lorem vel elit venenatis fringilla eget a felis. Aliquam sagittis, velit ac commodo ornare, turpis nisl volutpat orci, sed feugiat ligula augue et eros. Curabitur a magna sit amet diam dapibus euismod. Nulla iaculis dapibus purus, ut molestie nulla tempor ac. Maecenas aliquet mi diam. Duis convallis lorem sed magna venenatis, non sodales sem bibendum. Mauris posuere dolor quis nunc convallis lacinia. Phasellus tempor orci non nibh laoreet tempus. Sed pellentesque at leo ut pharetra. Ut venenatis arcu eros, id elementum felis elementum a. Nulla facilisi.

                        Aenean dignissim orci vel molestie tincidunt. Nunc faucibus ut ante in tempus. Ut semper interdum fermentum. Curabitur ut massa massa. Donec eu nulla efficitur, pulvinar justo id, viverra nunc. Mauris quis dapibus est. Sed tristique mauris vel nulla commodo, in euismod augue placerat. Fusce a felis elementum, sollicitudin sapien a, feugiat nulla. Integer nec placerat leo. Ut tempus libero diam, non pharetra elit euismod vitae. Praesent ultrices sem ac nibh accumsan lobortis. Curabitur pulvinar metus nec augue fringilla aliquam. Ut tempor erat eu mattis convallis. Curabitur fringilla magna ac turpis gravida tristique. Phasellus nisl metus, tincidunt vel ligula quis, accumsan dapibus lorem. Morbi maximus, quam eget efficitur congue, lorem nisi lobortis ante, non mattis tortor nulla eu lorem.

                        Donec non semper lorem. Maecenas consectetur augue non laoreet imperdiet. Quisque quam diam, gravida varius neque sed, vulputate convallis nisi. Vivamus pretium pretium tempor. Nulla eu efficitur ipsum. Ut in dapibus libero. Duis convallis elit et nisl dictum pharetra. Nullam et venenatis odio. Quisque commodo sagittis erat in aliquet. Proin condimentum felis sed maximus rhoncus"""
    

    agregar_data = file.write(agregar_texto)
 
    
file = open(ruta_absoluta, 'r')
leer_file = file.read()
file.close()
print(leer_file)
    

nueva_ruta = '/Users/dannygarcia/Desktop/tarea.txt'

copiar_file = open(nueva_ruta, 'wt')
copiar_file.write(agregar_texto)
copiar_file.close()
print(copiar_file)
    


 