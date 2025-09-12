import streamlit as st

st.title("実験紹介")

with st.container(border=True):
    st.header("内容")
    st.text(
        "本実験では、5〜10秒程度の発話音声を聞いていただき、その音声に関する質問にご回答ください。\n\n"
        "各音声に、以下に関する質問が用意されています。\n"
        "(1) イントネーションの自然さ：イントネーションがどのくらい自然に聞こえるかを評価してください。\n"
        "(2) 明瞭性：発話内容がどのくらい聞き取りやすいかを評価してください。\n"
        "(3) 類似度：2つの発話の声がどのくらい類似しているかを評価してください。\n\n"
        "各質問にはラジオボタン式の選択肢があります。\n"
        "もっとも当てはまるものを選択してください。\n"
        "(1) とても悪い　(2) 悪い　(3) 普通　(4) 良い　(5) とても良い"
        "\n\n"
        "音声は繰り返し聞くことが可能ですが、最大2回までとしてください。\n\n"
        "全部で40個の音声を聞いて評価していただきます。所要時間は15～20分程度です。"
    )

    st.header("インタフェース")
    st.text(
        "以下に、実際に使用していただくインターフェースの例を示します。\n\n"
        "- 音声を再生して、スピーカーの動作を事前に確認できます。\n\n"
        "- 画面が大きすぎる・小さすぎる場合は、ブラウザのズーム機能（Ctrl/CMD＋「+」「-」キー）で拡大・縮小してください。"
    )

    with st.container(border=True):
        st.text("音声を聞いていただき、質問にご回答ください。")
        st.text("音声A")
        st.audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/gt/audio/jvs001/099.wav"
        )
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
            horizontal=True,
        )
        st.text("音声B")
        st.audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/gt/audio/jvs001/098.wav"
        )
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
            horizontal=True,
        )

    st.warning(
        "音声を最後まで聞かず、ランダム的に回答されていると判断される場合は、報酬を支払えないことがあります。"
    )

next_button = st.button(label="実験へ")
if next_button:
    st.switch_page("pages/exp.py")
