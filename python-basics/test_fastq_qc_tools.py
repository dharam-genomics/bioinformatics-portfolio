import pytest
from fastq_qc_tools import check_qc, validate_record, FastqValidationError, count_reads, run_qc

@pytest.fixture
def data_dir(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    pass_file = data_dir / "good.fastq"

    fastq_content = """@read1
ATGC
+
!!!!
@read2
GCTA
+
####
@read3
ATGC
+
!!!!
@read4
GCTA
+
####
@read5
ATGC
+
!!!!
@read6
GCTA
+
####
@read7
ATGC
+
!!!!
@read8
GCTA
+
####
"""

    pass_file.write_text(fastq_content)

    fail_file = data_dir / "low_reads.fastq"

    fail_content = """@read1
ATGC
+
!!!!
@read2
GCTA
+
####
"""

    fail_file.write_text(fail_content)

    invalid_file = data_dir / "invalid.fastq"

    invalid_content = """@read1
ATGC
+
!!!
"""

    invalid_file.write_text(invalid_content)

    return data_dir

def test_run_qc(data_dir):

    results = run_qc(data_dir, minimum_reads=4)
    assert results["good.fastq"]["reads"] == 8
    assert results["low_reads.fastq"]["reads"] == 2
    assert results["good.fastq"]["status"] == "PASS"
    assert results["low_reads.fastq"]["status"] == "FAIL"
    assert results["invalid.fastq"]["status"] == "INVALID"

def test_check_qc_pass():
    result = check_qc(8, 6)
    assert result == "PASS"

def test_check_qc_fail():
    result = check_qc(4, 6)
    assert result == "FAIL"

def test_check_qc_boundary():
    result = check_qc(6, 6)
    assert result == "PASS"

def test_validate_record_invalid():
    with pytest.raises(FastqValidationError):
        validate_record("ATGC", "!!!")

def test_count_reads(tmp_path):
    fastq_file = tmp_path / "test.fastq"

    fastq_content = """@read1
ATGC
+
!!!!
@read2
GCTA
+
####
"""

    fastq_file.write_text(fastq_content)

    result = count_reads(fastq_file)

    assert result == 2

def test_count_reads_invalid(tmp_path):
    fastq_file = tmp_path / "invalid.fastq"

    fastq_content = """@read1
ATGC
+
!!!
"""

    fastq_file.write_text(fastq_content)

    with pytest.raises(FastqValidationError):
        count_reads(fastq_file)
