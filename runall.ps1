Write-Output "Empezando"

$Pythonscriptpath = "C:\Users\ypalacios\Desktop\Universidad\Taller4\taller4-GPI\"
& set-location $Pythonscriptpath

& conda env create -f environment.yml
& conda activate myenvironment
& cd ./scripts
& python Import_data_Zenodo.py
& python RL_Energia_gas.py
& python RL_Energia_carbon.py
& python RL_Energia_petroleo.py
& python RL_Energia_embalses.py
& cd ../


Write-Output "Listo!"