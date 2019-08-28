# Script for building quality check for BIDS

import os, glob

#def analyze_data():
    
def main():
    # get paths and subject directory paths
    BIDS_PATH = "/projects/niblab/bids_projects/Experiments/bro/BIDS"
    sub_dirs = glob.glob(os.path.join(BIDS_PATH, 'sub-*'))
    #print(sub_dirs)
    # get the multiple sessions
    sessions=['ses-1', 'ses-2']
    qa_dict = {}
    
    for sess_id in sessions:
        if sess_id not in qa_dict:
            qa_dict[sess_id] = {}
        for sub_path in sorted(sub_dirs):
            base_dir = os.path.join(sub_path, sess_id)
            if os.path.exists(base_dir):
                sub_id = sub_path.split("/")[-1]
                if sub_id not in qa_dict[sess_id]:
                    qa_dict[sess_id][sub_id] = { "FUNC": None, "ANAT": None, "FMAP": None }
                #CHECK FOR DIRECTORIES
                # func/
                # anat/
                # fmap/
        print("SESSION {} DICTIONARY: \n{}\n".format(sess_id,qa_dict[sess_id]))        
    #print("DIRECTORY PATH: ", base_dir)
main()