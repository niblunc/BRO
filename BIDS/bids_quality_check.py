# Script for building quality check for BIDS

import os, glob
import pandas as pd



def dict_make(sessions, sub_dirs):
    qa_dict = {}
    # loop through each sessions we have
    for sess_id in sessions:
        if sess_id not in qa_dict:
            qa_dict[sess_id] = {}
        # loop through subjects by their bids path
        for sub_path in sorted(sub_dirs):
            base_dir = os.path.join(sub_path, sess_id) 
            sub_id = sub_path.split("/")[-1]
            if sub_id not in qa_dict[sess_id]:
                qa_dict[sess_id][sub_id] = { "func": None, "runs_pe": None, "runs_train": None, "runs_rest": None, "anat": None, "fmap": None }
                #CHECK FOR DIRECTORIES
            # func/
            funcs_nii=glob.glob("/projects/niblab/bids_projects/Experiments/bro/bids_/{}/{}/func/*.nii.gz".format(sub_id, sess_id))
            #print(funcs_nii)
            nii_ct = len(funcs_nii)
            qa_dict[sess_id][sub_id]["func"] = nii_ct
            qa_dict[sess_id][sub_id]["runs_pe"] = len([x for x in funcs_nii if "-pe_" in x])
            qa_dict[sess_id][sub_id]["runs_train"] = len([x for x in funcs_nii if "training" in x])
            qa_dict[sess_id][sub_id]["runs_rest"] = len([x for x in funcs_nii if "resting" in x])
            # anat/
            anat_nii=glob.glob("/projects/niblab/bids_projects/Experiments/bro/bids_/{}/{}/anat/*.nii.gz".format(sub_id, sess_id))
            #print(anat_nii)
            nii_ct = len(anat_nii)
            qa_dict[sess_id][sub_id]["anat"] = nii_ct
            # fmap/
            fmap_nii=glob.glob("/projects/niblab/bids_projects/Experiments/bro/bids_/{}/{}/func/*.nii.gz".format(sub_id, sess_id))
            #print(fmap_nii)
            nii_ct = len(fmap_nii)
            qa_dict[sess_id][sub_id]["fmap"] = nii_ct
        
        print("SESSION {} DICTIONARY: \n{}\n".format(sess_id,qa_dict[sess_id]))
 
    return qa_dict
        
        
def analyze_data(qa_dict):
    for sess_id in qa_dict:
        df = pd.DataFrame(qa_dict[sess_id])
        print(df.head())
        df.T.to_csv("bro_bids_{}.csv".format(sess_id), sep="\t")
    
def main():
    # get paths and subject directory paths
    BIDS_PATH = "/projects/niblab/bids_projects/Experiments/bro/bids_"
    sub_dirs = glob.glob(os.path.join(BIDS_PATH, 'sub-*'))
    #print(sub_dirs)
    # get the multiple sessions
    sessions=['ses-1', 'ses-2']
    qa_dict = dict_make(sessions, sub_dirs) 
    analyze_data(qa_dict)
main()