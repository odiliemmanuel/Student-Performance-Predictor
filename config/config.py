from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "student_data.xlsx"

TARGET_COLUMN = "final_grade"
TEST_SIZE = 0.2
RANDOM_STATE = 42

COLUMN_RENAME_MAP = {
    "famsize": "family_size",
    "Pstatus": "parents_living_status",
    "Medu": "mother_education",
    "Fedu": "father_education",
    "Mjob": "mother_job",
    "Fjob": "father_job",
    "traveltime": "travel_time",
    "studytime": "study_time",
    "failures": "number_of_past_class_failures",
    "schoolsup": "school_support",
    "famsup": "family_support",
    "paid": "extra_paid_classes",
    "activities": "extra_curricular_activities",
    "nursery": "attended_nursery_school",
    "higher": "wants_to_take_higher_education",
    "internet": "internet_access_at_home",
    "romantic": "in_a_romantic_relationship",
    "famrel": "quality_of_family_relationships",
    "freetime": "free_time_after_school",
    "goout": "going_out_with_friends",
    "Dalc": "workday_alcohol_consumption",
    "Walc": "weekend_alcohol_consumption",
    "health": "current_health_status",
    "absences": "number_of_school_absences",
    "G1": "first_period_grade",
    "G2": "second_period_grade",
    "G3": "final_grade",
}