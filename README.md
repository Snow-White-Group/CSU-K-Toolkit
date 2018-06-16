# CSU-K-Toolkit
This is the CSU-K toolkit for spoken call shared task 2. It contains several scripts, models and other data. Those files have been used to develop our two CSU-K ST2 systems, which you can find here:

* [CSU-K-DNN-Based-System](https://github.com/Snow-White-Group/The-CSU-K-DNN-Based-System-for-the-2nd-Edition-Spoken-CALL-Shared-Task)
* [CSU-K-Rule-Based-System](https://github.com/Snow-White-Group/The-CSU-K-Rule-Based-System-for-the-2nd-Edition-Spoken-CALL-Shared-Task)

Furthermore there is a tutorial paper, which explains the shared task and our systems in more detail:

* [Tutorial paper](https://github.com/Snow-White-Group/CSU-K-Toolkit/blob/master/CSU-K-ST2-Tutorial.pdf), please note that this is not an officially published paper


|  Order   | ScriptName                                   | Input                                      |   Output                                                                        |   notes                                                         |
|  ------- | -------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|  1, c    | generateDistanceVectors.py                   | Doc2Vec, ReferenceGrammer, RecResult       |   X-Vectors as CSV                                                              |                                                                 |
|  a       | generateDoc2VecModel.py                      | Dir to Training Text                       |   a Doc2Vec Model                                                               |                                                                 |
|  b       | split_file.py                                | Training CSV, Modulator                    |   Train and Test                                                                |   you can use another split script                              |
|  d       | makeLabelsFromCSV.py                         | Test or Test CSV                           |   Y-Vectors as CSV                                                              |                                                                 |
|  opt     | splitBasedOnIdFile.py                        | Txt containing ids, file you want to split |   Two files one only contraining ids from input txt                             |   alternative to b                                              |
|  opt     | split_csv_by_mod_10.py                       | Training CSV                               |   Train and Test where Test ist 10% of Train                                    |   alternative to b                                              |
|  opt     | makeLabelsFromCSV_v2.py                      | Test CSV from ST2                          |   Y-Vectors as CSV                                                              |                                                                 |
|  help    | validateUniqueIds.py                         | As many files as you like                  |   IDs that are shared                                                           |   check if you have clean train and test                        |
|  help    | extractBaseOnId.py                           | Txt containing ids, some file              |   Two files like the secound input file. But one just containg the ids from txt |   if you have messed up something                               |
|  help    | merge_sc_1_training_data_with_asr.py         | Train CSV, ASR, ASR_Data                   |   sc1 train entries are have asr output as rec_result                           |                                                                 |
|  help    | merge_sc_2_training_data_with_asr.py         | Test CSV, ASR, ASR_Data                    |   sc2 train entries,are have asr output as rec_result                           |                                                                 |
|  help    | normalize_sc_1_test.py                       | ABC CSV files, Outputfile                  |   CSV file formatted like sc1_train                                             |                                                                 |
|  help    | normalize_sc_2_abc.py                        | Test CSV, Outputfile                       |   CSV file formatted like sc1_train                                             |                                                                 |
|  help    | get_intersected_ids.py                       | A lot of CSV                               |   intersacting ids                                                              |                                                                 |
|  help    | fix_id_in_csv.py                             | Data CSV, Outputfile                       |   same as input but with fixed ids                                              |                                                                 |
|  exp     | generateWord2VecModel.py                     | Dir with Training Text                     |   a Word2Vec Model                                                              |                                                                 |
|  exp     | makeMeaningLabelsFromCSV.py                  | Data CSV                                   |   File with Meaning Labels                                                      |                                                                 |
|  exp     | makeMeaningLabelsFromCSV.py                  | Data CSV                                   |   File with Meaning Labels                                                      |                                                                 |
|  exp     | makeGrammarLabelFromCSV.py                   | Data CSV                                   |   File with Grammer Labels                                                      |                                                                 |
|  exp     | split_ABC_intelligent.py                     | Data CSV A B and C                         |   Several files needed by ASR. Creates scp files, spk2utt, utt2spk and text     |   Use with caution. You should already have most of those files |
