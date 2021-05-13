

import pandas as pd

import os, glob


bids_dict = {"ses1": {}, "ses2": {}}
subs=glob.glob("sub-*")

ses1=glob.glob('sub-*/ses-1')
ses2=glob.glob('sub-*/ses-2')

for s in sorted(ses1):
    funcs=glob.glob(os.path.join(s, "func/*"))
    anat=glob.glob(os.path.join(s, "anat/*"))
    fmap=glob.glob(os.path.join(s, "fmap/*"))
    _id = s.split("/")[0]
    if _id not in bids_dict["ses1"]:
        bids_dict["ses1"][_id] = {}
    bids_dict["ses1"][_id]["FUNC"]=funcs
    bids_dict["ses1"][_id]["ANAT"]=anat
    bids_dict["ses1"][_id]["FMAP"]=fmap
for s in sorted(ses2):
    funcs=glob.glob(os.path.join(s, "func/*"))
    anat=glob.glob(os.path.join(s, "anat/*"))
    fmap=glob.glob(os.path.join(s, "fmap/*"))
    _id = s.split("/")[0]
    if _id not in bids_dict["ses2"]:
        bids_dict["ses2"][_id] = {}
    bids_dict["ses2"][_id]["FUNC"]=funcs
    bids_dict["ses2"][_id]["ANAT"]=anat
    bids_dict["ses2"][_id]["FMAP"]=fmap

df_s1=pd.DataFrame(bids_dict['ses1'])
df_s2=pd.DataFrame(bids_dict['ses2'])

df_s1.T.to_csv("/projects/niblab/bids_projects/Experiments/bro/bids/derivatives/bids_s1.csv", sep="\t")
df_s2.T.to_csv("/projects/niblab/bids_projects/Experiments/bro/bids/derivatives/bids_s2.csv", sep="\t")
