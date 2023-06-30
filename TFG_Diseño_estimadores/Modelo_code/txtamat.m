[nombre, directorio] = uigetfile('MultiSelect', 'on'); %selecciono los archivos txt
nombre = cellstr(nombre); %crea un cell array
for n = 1:length(nombre)
  previo = fullfile(directorio, nombre{n});
  data = importdata(previo);
  % Elimina la extensión del archivo
  [vacio, nuevo] = fileparts(nombre{n});
  save(nuevo, 'data');
end