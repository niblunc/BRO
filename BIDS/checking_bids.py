## Check what subjects have been converted to BIDS and which haven't

import glob, os
import subprocess
import pandas as pd 

bids_dir_path = "/projects/niblab/bids_projects/Experiments/BRO/BIDS"
dcm_dir_path = "/projects/niblab/bids_projects/Experiments/BRO/DICOM"

multi_sess = True
RUN_BIDS = False 
gen_report = True

def generate_report(bids_dict, multi_sess):
    if multi_sess==True:
        print("BIDS Subjects -")
        for sess in bids_dict:
            sub_string = ",".join(sorted(bids_dict[sess]))
            print("SESSION %s | SUBJECT COUNT %s:"%(sess.split("-")[1], len(bids_dict[sess])))
            print(sub_string)
        
if multi_sess == True:
    sessions = ["ses-1", "ses-2"]
    bids_subjects = {}
    dcm_subjects = {}
    for sess in sessions:
        bids_subjects[sess] = [x.split("/")[-2] for x in glob.glob(os.path.join(bids_dir_path, "sub-*", sess))]
        dcm_subjects[sess] = [x.split("/")[-1] for x in glob.glob(os.path.join(dcm_dir_path, sess, 'sub-*'))]
        
    df_dict = {}
    
    
    for sess in bids_subjects:
        bids = bids_subjects[sess]
        dcm = dcm_subjects[sess]
        missing = [x for x in dcm if x not in bids]
        print("Subjects from SESSION %s that need conversion:"%sess.split("-")[1], missing) 
        if RUN_BIDS == True:
            sub_ids =" ".join([x.split("-")[1] for x in missing])
            print(sub_ids)
            BATCH_CMD = "/projects/niblab/bids_projects/Experiments/BRO/BIDS/code/bids_template.job"
            BIDS_CMD = "singularity exec -B /:/base_dir /projects/niblab/bids_projects/Singularity_Containers/heudiconv_05_2019.simg \
heudiconv -b -d /base_dir/projects/niblab/bids_projects/Experiments/BRO/DICOM/ses-{session}/sub-{subject}/*dcm -s %s -ss %s \
-f /base_dir/projects/niblab/bids_projects/Experiments/BRO/BIDS/code/BRO_heuristic.py \
-c dcm2niix -o /base_dir/projects/niblab/bids_projects/Experiments/BRO/BIDS"%(sub_ids,sess.split("-")[1])
            print(BIDS_CMD)
            run_batch = subprocess.Popen(["sbatch", BATCH_CMD, BIDS_CMD])

    if gen_report == True:
        generate_report(bids_subjects, multi_sess)
        