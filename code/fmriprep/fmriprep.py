import os, glob

# gather subjects 
bids_dir_path = "/projects/niblab/bids_projects/Experiments/BRO/BIDS"

subjects = sorted([x.split("/")[-1] for x in glob.glob(os.path.join(bids_dir_path, "sub-*"))])

subjects_string = " ".join(subjects)


fmriprep_cmd = 'singularity exec -B /projects/niblab/bids_projects:/base_dir -B /projects/niblab/bids_projects/mytemplateflowdir:/opt/templateflow /projects/niblab/bids_projects/Singularity_Containers/fmriprep_v2_2019.simg \
fmriprep /base_dir/Experiments/BRO/BIDS /base_dir/Experiments/BRO/fmriprep \
    participant  \
    --participant-label %s  \
    --skip_bids_validation \
    --fs-license-file /base_dir/freesurfer/license.txt \
    --fs-no-reconall \
    --omp-nthreads 16 --n_cpus 16 \
    --ignore slicetiming  \
    --bold2t1w-dof 12 \
    --output-spaces MNI152Lin \
     -w /base_dir/Experiments/BRO/fmriprep \
     --resource-monitor --write-graph --stop-on-first-crash'%subjects_string

