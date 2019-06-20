import glob, os


# Get the paths and subjects
bids_dir_path = "/projects/niblab/bids_projects/Experiments/BRO/BIDS"
subject_list = sorted(glob.glob(os.path.join(bids_dir_path, "sub-*")))

# Loop through subjects
for subj_path in subject_list:
    sub_id = subj_path.split("/")[-1]
    session_list = glob.glob(os.path.join(subj_path, "ses-*"))
    for sess_path in session_list:
        sess_id = sess_path.split("/")[-1]
        anat_file_path=os.path.join(sess_path, "anat", "%s_%s_T1w.nii.gz"%(sub_id, sess_id)
        func_list=glob.glob(os.path.join(sess_path, "func", "*.nii.gz"))
        fmap_list=glob.glob(os.path.join(sess_path, "fmap", "*"))
        if not os.path.exists(anat_file_path):
            #NO ANATS
        # Functional to expect: task-pe(2), task-resting(1), task-training(2)
        if len(func_list) != 5:
            #ERROR WITH FUNC
            if len(func_list) > 5:
                #EXTRA RUN
            if len(func_list) < 5:
                #MISSING RUN
        if not fmap_list:
            #NO FMAPS
            
            