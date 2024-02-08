This readme explains generate random data and instrucions, and how to test them
*Please note that you may need to change 'python' to 'python3' based on which system the code is running at*

To generate data and instructions:
1. cd into data_generation
2. run 'python data_gen.py'
3. enter data size

To test the new data:
1. cd back into parent folder 'Assign1-sxxxx-sxxxx'
2. run 'python dictionary_test_script.py $PWD <dictionary_type> $PWD/data_generation/data<data_size>.txt $PWD/data_generation/test<data_size>.in'

If you would like to see the timing part in action, please replace the script files in 'Assign1-sxxxx-sxxxx' folder to scripts in /TIMING_SCRIPTS
