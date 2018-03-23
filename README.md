# CSU-K-Toolkit
This is the CSU-K toolkit for spoken call shared task 2. It contains several scripts, models and other data.

```
  Order   ScriptName                                   Input                                        Output                                                                          notes
  ------- -------------------------------------------- -------------------------------------------- ------------------------------------------------------------------------------- ---------------------------------------------------------------
  1, c    generateDistanceVectors.py                   Doc2Vec, ReferenceGrammer, RecResult         X-Vectors as CSV                                                                
  a       generateDoc2VecModel.py                      Dir to Training Text                         a Doc2Vec Model                                                                 
  b       split\_file.py                               Training CSV, Modulator                      Train and Test                                                                  you can use another split script
  d       makeLabelsFromCSV.py                         Test or Test CSV                             Y-Vectors as CSV                                                                
  opt     splitBasedOnIdFile.py                        Txt containing ids, file you want to split   Two files one only contraining ids from input txt                               alternitive to b
  opt     split\_csv\_by\_mod\_10.py                   Training CSV                                 Train and Test where Test ist 10% of Train                                      alternitive to b
  opt     makeLabelsFromCSV\_v2.py                     Test CSV from ST2                            Y-Vectors as CSV                                                                
  help    validateUniqueIds.py                         As many files as you like                    IDs that are shared                                                             check if you have clean train and test
  help    extractBaseOnId.py                           Txt containing ids, some file                Two files like the secound input file. But one just containg the ids from txt   if you have messed up something
  help    merge\_sc\_1\_training\_data\_with\_asr.py   Train CSV, ASR, ASR\_Data                    sc1 train entries are have asr output as rec\_result                            
  help    merge\_sc\_2\_training\_data\_with\_asr.py   Test CSV, ASR, ASR\_Data                     sc2 train entries,are have asr output as rec\_result                            
  help    normalize\_sc\_1\_test.py                    ABC CSV files, Outputfile                    CSV file formatted like sc1\_train                                              
  help    normalize\_sc\_2\_abc.py                     Test CSV, Outputfile                         CSV file formatted like sc1\_train                                              
  help    get\_intersected\_ids.py                     A lot of CSV                                 intersacting ids                                                                
  help    fix\_id\_in\_csv.py                          Data CSV, Outputfile                         same as input but with fixed ids                                                
  exp     generateWord2VecModel.py                     Dir with Training Text                       a Word2Vec Model                                                                
  exp     makeMeaningLabelsFromCSV.py                  Data CSV                                     File with Meaning Labels                                                        
  exp     makeGrammarLabelFromCSV.py                   Data CSV                                     File with Grammer Labels                                                        
  exp     split\_ABC\_intelligent.py                   Data CSV A B and C                           Several files needed by ASR. Creates scp files, spk2utt, utt2spk and text       Use with caution. You should already have most of those files
```
