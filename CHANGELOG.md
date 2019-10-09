# Changelog - BRO
All notable changes to this project will be documented in this file.  


The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## 2019-09-01  
### Added
- ses-1: 43 subjects in BIDS format available
- ses-2: 50 subjects in BIDS format available

### Changed
- sub-009: removed run-1 training task files in each session for bad volumes, extra run was available and used for replacement.  
- sub-047: removed run-1 training task files for ses-1, extra run was available for replacement.
- sub-050: for ses-1, 5 runs were available for pe task, first 3 had bad volumes, 4 and 5 are good. For ses-2, run-1 for training task had bad volumes, extra run was available for replacement.
- sub-051: ses-1, 4 runs available for task pe, run-1 and run-3 had bad volumes, run-2 and run-4 are used for replacements.
- sub-056: ses-1, run-2 file for pe task removed for bad volumes, replacement run unavailable.
- sub-016: ses-2, run-1 had bad volumed, was removed, extra runs were available for replacement.
- sub-023: ses-2, run-1 training task file removed for bad volume, replacement run unavailable.
- sub-034: ses-2, run-2 pe task file removed for bad volume, replacement run file was available.
- sub-039: ses-2, run-2 training task file removed for bad volume, replacement run file was available.
- sub-041: ses-2, run-2 training task file removed for bad volume, replacement run file was available.

### Errors
- sub-020: only 1 run for both training and pe tasks, volume for pe task is bad.
  * `File:sub-020_ses-1_task-pe_run-1_bold.nii.gz | Volume:50`  
- sub-031: bad volumes for both training runs, ses-1, replacement runs unavailable.
  * `File:sub-031_ses-1_task-training_run-1_bold.nii.gz | Volume:228`  
  * `File:sub-031_ses-1_task-training_run-2_bold.nii.gz | Volume:231`

- sub-055: bad volumes for all available runs for traning and pe tasks, ses-1  
  * `File:sub-055_ses-1_task-training_run-1_bold.nii.gz | Volume:239`
  * `File:sub-055_ses-1_task-training_run-2_bold.nii.gz | Volume:237`
  * `File:sub-055_ses-1_task-pe_run-1_bold.nii.gz | Volume:190`
  * `File:sub-055_ses-1_task-pe_run-2_bold.nii.gz | Volume:192`

- sub-056: ses-1, run-2 for pe task had bad volumes, replacement run unavailable
- sub-023: ses-2, run-1 training task file removed for bad volume, replacement run unavailable
  * `File:sub-023_ses-2_task-training_run-1_bold.nii.gz | Volume:213`

## 2019-06-01  
### Added  
- BIDS conversion for added subjects
    - SESSION 1, SUBJECT COUNT 30
        * AVAILABLE SUBJECTS: sub-001,sub-002,sub-003,sub-006,sub-008,sub-009,sub-010,sub-011,sub-012,sub-014,sub-015,sub-016,sub-028,sub-029,sub-030,sub-031,sub-032,sub-033,sub-034,sub-036,sub-038,sub-040,sub-043,sub-044,sub-045,sub-046,sub-047,sub-048,sub-051,sub-052
    - SESSION 2, SUBJECT COUNT 34
        * AVAILABLE SUBJECTS: sub-001,sub-002,sub-003,sub-006,sub-008,sub-009,sub-010,sub-011,sub-012,sub-014,sub-015,sub-016,sub-023,sub-028,sub-030,sub-031,sub-032,sub-033,sub-034,sub-036,sub-038,sub-040,sub-041,sub-042,sub-043,sub-044,sub-045,sub-046,sub-047,sub-048,sub-049,sub-050,sub-051,sub-052

### Errors
- Current error #1: `1: [ERR] You have to define 'EchoTime1' and 'EchoTime2' for this file. (code: 15 - ECHO_TIME1-2_NOT_DEFINED)
		./sub-008/ses-2/fmap/sub-008_ses-2_phasediff.nii.gz
		./sub-010/ses-1/fmap/sub-010_ses-1_phasediff.nii.gz
		./sub-037/ses-1/fmap/sub-037_ses-1_phasediff.nii.gz
		./sub-052/ses-1/fmap/sub-052_ses-1_phasediff.nii.gz
		./sub-055/ses-1/fmap/sub-055_ses-1_phasediff.nii.gz`
- sub-037/ses-1 and sub-052 did not make functionals -- need to inspect/re-run
- sub-012 anat error
