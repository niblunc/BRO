# Changelog - BRO
All notable changes to this project will be documented in this file.  
  
  
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2019-09-01  
### Added 

  
## [0.0.1] - 2019-06-01  
### Added  
- BIDS conversion for added subjects
    - SESSION 1, SUBJECT COUNT 30
        * AVAILABLE SUBJECTS: sub-001,sub-002,sub-003,sub-006,sub-008,sub-009,sub-010,sub-011,sub-012,sub-014,sub-015,sub-016,sub-028,sub-029,sub-030,sub-031,sub-032,sub-033,sub-034,sub-036,sub-038,sub-040,sub-043,sub-044,sub-045,sub-046,sub-047,sub-048,sub-051,sub-052
    - SESSION 2, SUBJECT COUNT 34
        * AVAILABLE SUBJECTS: sub-001,sub-002,sub-003,sub-006,sub-008,sub-009,sub-010,sub-011,sub-012,sub-014,sub-015,sub-016,sub-023,sub-028,sub-030,sub-031,sub-032,sub-033,sub-034,sub-036,sub-038,sub-040,sub-041,sub-042,sub-043,sub-044,sub-045,sub-046,sub-047,sub-048,sub-049,sub-050,sub-051,sub-052

### Errors
Current error #1: `1: [ERR] You have to define 'EchoTime1' and 'EchoTime2' for this file. (code: 15 - ECHO_TIME1-2_NOT_DEFINED)
		./sub-008/ses-2/fmap/sub-008_ses-2_phasediff.nii.gz
		./sub-010/ses-1/fmap/sub-010_ses-1_phasediff.nii.gz
		./sub-037/ses-1/fmap/sub-037_ses-1_phasediff.nii.gz
		./sub-052/ses-1/fmap/sub-052_ses-1_phasediff.nii.gz
		./sub-055/ses-1/fmap/sub-055_ses-1_phasediff.nii.gz`

### Errors
- sub-037/ses-1 and sub-052 did not make functionals -- need to inspect/re-run
- sub-012 anat error
