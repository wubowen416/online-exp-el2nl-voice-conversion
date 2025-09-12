import numpy as np
import streamlit as st

# np.random.seed(1234)


def get_url(idx: str, name: str, hid: str):
    url = f"https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/{name}/audio/jvs{hid}/{idx}.wav"
    return url


if "samples" not in st.session_state:
    idcs = ["001", "011", "017", "021", "025"]  # , "035", "036", "058", "065", "071"]
    hids = ["001", "021", "041", "061", "081"]  # , "001", "021", "041", "061", "081"]
    samples = []
    for idx, hid in zip(idcs, hids):
        for name in ["gt", "qvc_base", "qvc_ft_10k", "qvc_ft_pair_flat_10k"]:
            samples.append(
                {
                    "url": get_url(idx, name, hid),
                    "sim_url": get_url("100", "gt", hid),  # for similarity comparison
                    "model_name": name,
                    "idx": idx,
                }
            )
    np.random.shuffle(samples)
    st.session_state["samples"] = samples
if "num_samples" not in st.session_state:
    st.session_state["num_samples"] = len(st.session_state["samples"])
if "sample_idx" not in st.session_state:
    st.session_state["sample_idx"] = 0
if "results" not in st.session_state:
    st.session_state["results"] = {"nat": [], "int": [], "sim": []}


def choice_to_value(choice: str) -> int:
    value = 3
    match choice:
        case "とても悪い":
            value = 1
        case "悪い":
            value = 2
        case "良い":
            value = 4
        case "とても良い":
            value = 5
    return value


def on_form_submitted():
    # Record choice
    nat_value = choice_to_value(
        st.session_state[f'nat_choice_{st.session_state["sample_idx"]}']
    )
    int_value = choice_to_value(
        st.session_state[f'int_choice_{st.session_state["sample_idx"]}']
    )
    sim_value = choice_to_value(
        st.session_state[f'sim_choice_{st.session_state["sample_idx"]}']
    )
    st.session_state["results"]["nat"].append(nat_value)
    st.session_state["results"]["int"].append(int_value)
    st.session_state["results"]["sim"].append(sim_value)

    # Move to next pair
    st.session_state["sample_idx"] += 1


# Interface
st.title("実験")
st.warning(
    "ページを更新したりタブを閉じたりしないでください。入力済みのデータが失われます。"
)
progress_bar_text = "進捗"
progress_bar = st.progress(
    0, text=f"{progress_bar_text}: {0}/{st.session_state['num_samples']}"
)


@st.fragment
def exp_fragment():
    # Check if all completed
    if st.session_state["sample_idx"] == st.session_state["num_samples"]:
        st.switch_page("pages/comment.py")

    # Get sample info
    sample = st.session_state["samples"][st.session_state["sample_idx"]]
    url = sample["url"]
    sim_url = sample["sim_url"]

    # Place interface
    with st.container(border=True):
        st.text(f"音声を聞いていただき、質問にご回答ください。")
        st.text("音声A")
        st.audio(url)
        nat_choice = st.radio(
            "Q1: 音声Aについて、イントネーションの自然さはどう思いますか？",
            options=[
                "とても悪い",
                "悪い",
                "普通",
                "良い",
                "とても良い",
            ],
            index=None,
            key=f'nat_choice_{st.session_state["sample_idx"]}',
            horizontal=True,
        )
        int_choice = st.radio(
            "Q2: 音声Aについて、明瞭性、聞き取りやすさはどう思いますか？",
            options=[
                "とても悪い",
                "悪い",
                "普通",
                "良い",
                "とても良い",
            ],
            index=None,
            key=f'int_choice_{st.session_state["sample_idx"]}',
            horizontal=True,
        )
        st.text("音声B")
        st.audio(sim_url)
        sim_choice = st.radio(
            "Q3: 音声AとBについて、声の類似度はどう思いますか",
            options=[
                "とても悪い",
                "悪い",
                "普通",
                "良い",
                "とても良い",
            ],
            index=None,
            key=f'sim_choice_{st.session_state["sample_idx"]}',
            horizontal=True,
        )
        choice_has_not_been_made = (
            nat_choice is None or int_choice is None or sim_choice is None
        )
        st.button(
            "次へ",
            on_click=on_form_submitted,
            disabled=choice_has_not_been_made,
            help="質問にご回答ください" if choice_has_not_been_made else "",
        )

    progress_bar.progress(
        st.session_state["sample_idx"] / st.session_state["num_samples"],
        f"{progress_bar_text}: {st.session_state['sample_idx']}/{st.session_state['num_samples']}",
    )


exp_fragment()
