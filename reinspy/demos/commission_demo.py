from reinspy.commission import SlidingScale

sliding_scale = SlidingScale(
    rules=(
        [.25, .35, .45],
        [.60, .50, .30],
        [.01, .005]
    )
)
