import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import os, glob
import pandas as pd
from IPython.display import SVG, display

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

subjects = ['sub-001', 'sub-002', 'sub-003', 'sub-004', 'sub-005', 'sub-006', 'sub-007',
            'sub-008', 'sub-009', 'sub-010', 'sub-011', 'sub-012', 'sub-013', 'sub-014',
            'sub-015', 'sub-016', 'sub-017', 'sub-018', 'sub-019', 'sub-020', 'sub-021',
            'sub-022', 'sub-023', 'sub-024', 'sub-025', 'sub-026', 'sub-027', 'sub-028',
            'sub-029', 'sub-030', 'sub-031', 'sub-032', 'sub-033', 'sub-034', 'sub-035',
            'sub-036', 'sub-037', 'sub-038', 'sub-039', 'sub-040', 'sub-041', 'sub-042',
            'sub-043', 'sub-044', 'sub-045', 'sub-046', 'sub-047', 'sub-048', 'sub-049',
            'sub-050', 'sub-051', 'sub-052', 'sub-053', 'sub-054', 'sub-055', 'sub-056']








images_path = '/content/gdrive/My Drive/Projects/bromo/data/reports/fmri_images'
images=glob.glob(os.path.join(images_path, "*.svg"))

options=[ "ALL", "fieldmap", "flirtbbr", "brain mask", "sdc", 'anat',]
sessions=["ses-1", "ses-2"]
tasks = ['pe', 'training']
runs=['run-1', 'run-2']




def show_svg(image, subject, session, task,run):
    if image=="fieldmap":
        filename='{}_{}_task-{}_{}_desc-fieldmap_bold.svg'.format(subject, session, task, run)
        filepath = os.path.join(images_path, filename)
        try:
            print("\nEPI: \n")
            display(SVG(filename=filepath))
            print("FILE: {} \n".format(filename))
        except:
            print('image {} unavailable'.format(filename))

    elif image=='flirtbbr':
        filename='{}_{}_task-{}_{}_desc-flirtbbr_bold.svg'.format(subject, session, task, run)
        filepath = os.path.join(images_path, filename)
        try:
            print("\nFLIRTBBR: \n")
            display(SVG(filename=filepath))
            print("FILE: {} \n".format(filename))

        except:
            print('image {} unavailable'.format(filename))

    elif image=='anat':
        #sub-030_space-MNI152NLin2009cAsym_T1w.svg

        filename='{}_space-MNI152NLin2009cAsym_T1w.svg'.format(subject)
        filepath = os.path.join(images_path, filename)
        try:
            print("\nANAT T1w: \n")
            display(SVG(filename=filepath))
            print("FILE: {} \n".format(filename))

        except:
            print('image {} unavailable'.format(filename))

    elif image == 'brain mask':
        filename='{}_{}_desc-brain_mask.svg'.format(subject, session)
        filepath = os.path.join(images_path, filename)
        try:
            print("\nBrain Mask: \n")
            display(SVG(filename=filepath))
            print("FILE: {} \n".format(filename))
        except:
            print('image {} unavailable'.format(filename))

    elif image=='sdc':
        filename='{}_{}_task-{}_{}_desc-sdc_bold.svg'.format(subject, session, task, run)
        filepath = os.path.join(images_path, filename)
        try:
            print("\nSDC: \n")
            display(SVG(filename=filepath))
            print("FILE: {} \n".format(filename))
        except:
            print('image {} unavailable'.format(filename))


    elif image=="ALL":

        anat_filename='{}_space-MNI152NLin2009cAsym_T1w.svg'.format(subject)
        anat_filepath = os.path.join(images_path, anat_filename)
        try:
            print("\nANAT T1w: \n")
            display(SVG(filename=anat_filepath))
            print("FILE: {} \n".format(anat_filename))
            print("\n\n")
        except:
            print('image {} unavailable'.format(anat_filename))


        sdc_filename='{}_{}_task-{}_{}_desc-sdc_bold.svg'.format(subject, session, task, run)
        sdc_filepath = os.path.join(images_path, sdc_filename)
        try:
            print("SDC \n")
            display(SVG(filename=sdc_filepath))
            print("FILE: ", sdc_filename)
            print("\n\n")
        except:
            print('image {} unavailable'.format(sdc_filename))


        flirt_filename='{}_{}_task-{}_{}_desc-flirtbbr_bold.svg'.format(subject, session, task, run)
        flirt_filepath = os.path.join(images_path, flirt_filename)

        try:
            print("FLIRT: \n")
            display(SVG(filename=flirt_filepath))
            print("FILE: ", flirt_filename)
            print("\n\n")
        except:
            print('image {} unavailable'.format(flirt_filename))


        mask_filename='{}_{}_desc-brain_mask.svg'.format(subject, session)
        mask_filepath = os.path.join(images_path, mask_filename)
        try:
            print("Brain Mask: \n")
            display(SVG(filename=mask_filepath))
            print("FILE: ", mask_filename)
            print("\n\n")
        except:
            print('image {} unavailable'.format(mask_filename))


        field_filename='{}_{}_task-{}_{}_desc-fieldmap_bold.svg'.format(subject, session, task, run)
        field_filepath = os.path.join(images_path, field_filename)
        try:
            print("FIELDMAP: \n")
            display(SVG(filename=field_filepath))
            print("FILE: ", field_filename)
            print("\n\n")
        except:
            print('image {} unavailable'.format(field_filename))


    else:
        pass




@interact
def show_func_images(image=options, subject=subjects,session=sessions, task=tasks, run=runs):
    show_svg(image, subject,session, task, run)
