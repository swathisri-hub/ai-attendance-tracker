def predict_attendance(attendance):
    attendance = float(attendance)

    if attendance < 75:
        return "AT RISK"
    else:
        return "SAFE"
